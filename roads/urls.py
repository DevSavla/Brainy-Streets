from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('landing/', views.landing, name="landing"),
    path('harp/', views.harp, name="harp"),
    path('api/weather/', views.WeatherData.as_view(), name="weather"),
    re_path(r'^api/get-geojson/(?P<latitude>\d+\.\d+)/(?P<longitude>\d+\.\d+)/$', views.GetGeoJson.as_view(), name="get-geojson"),
    path('api/new-road/', views.NewRoad.as_view(), name="new-road")
]
