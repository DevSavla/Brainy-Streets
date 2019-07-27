
var platform = new H.service.Platform({
    'apikey': 'wGiMGJ08JeH-vLU5d9E1w_v_h0AyvMbLgn69GN6qen0'
});

var geocoder = platform.getGeocodingService();

// Gives user's location
if(navigator.geolocation) {

    navigator.geolocation.getCurrentPosition(position => {

        console.log(position);

        // Get address from lat and long
        geocoder.reverseGeocode(
            {
                mode: "retrieveAddresses",
                maxresults: 1,
                prox: position.coords.latitude.toString() + ',' + position.coords.longitude.toString()
            }, data => {
                document.getElementById('userlocation').innerHTML = data.Response.View[0].Result[0].Location.Address.Label;
            }, error => {
                console.error(error);
            }
        );

        // Instantiate (and display) a map object:
        newmap(position.coords.latitude, position.coords.longitude);
    });
}

function newmap(latitude, longitude) {
    const canvas = document.getElementById('map');
    const map = new harp.MapView({
    canvas,
    theme: "https://unpkg.com/@here/harp-map-theme@latest/resources/berlin_tilezen_night_reduced.json",
    //For tile cache optimization:
    maxVisibleDataSourceTiles: 40,
    tileCacheSize: 100
    });

    map.setCameraGeolocationAndZoom(
        new harp.GeoCoordinates(latitude, longitude),
        16
    );

    console.log(latitude, longitude);

    const mapControls = new harp.MapControls(map);
    const ui = new harp.MapControlsUI(mapControls);
    canvas.parentElement.appendChild(ui.domElement);

    mapControls.maxPitchAngle = 90;
    mapControls.setRotation(0,50);

    map.resize(window.innerWidth, window.innerHeight);
    window.onresize = () => map.resize(window.innerWidth, window.innerHeight);

    const omvDataSource = new harp.OmvDataSource({
    baseUrl: "https://xyz.api.here.com/tiles/herebase.02",
    apiFormat: harp.APIFormat.XYZOMV,
    styleSetName: "tilezen",
    authenticationCode: 'AOSoVWzHTbZ1FI7p9W795eI',
    });

    map.addDataSource(omvDataSource);

    fetch(window.location.href.split('/').slice(0,3).join('/')+'/api/get-geojson/')
    .then(data => data.json())
    .then(data => {
    const geoJsonDataProvider = new harp.GeoJsonDataProvider("wireless-hotspots", data);
    const geoJsonDataSource = new harp.OmvDataSource({
        dataProvider: geoJsonDataProvider,
        name: "wireless-hotspots",
        //styleSetName: "wireless-hotspots" NOTE: Not necessary here. For use if you want to add your style rules in the external stylesheet.
    });

    map.addDataSource(geoJsonDataSource).then(() => {
        const styles = [{
           when: "$geometryType == 'point'",
           technique: "circles",
           renderOrder: 10000,
           attr: {
              color: "#7ED321",
              size: 15
           }
        },
        {
            "when": "$geometryType ^= 'line'",
            "renderOrder": 1000,
            "technique": "solid-line",
            "attr": {
               "color": "#D73060",
               "transparent": true,
               "opacity": 1,
               "metricUnit": "Pixel",
               "lineWidth": 10
            }
         }
        ]
        geoJsonDataSource.setStyleSet(styles);
        map.update();
     });
    })
}