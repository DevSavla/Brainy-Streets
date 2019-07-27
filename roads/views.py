from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import *
from django.contrib.auth import logout, authenticate, login

from rest_framework.authtoken.models import Token
from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication

import datetime
import json

def home(request):
    return render(request, 'index.html')

def harp(request):
    return render(request, 'harp.html')

def datadetails(request):
    return render(request, 'datadetails.html')

class SaveData(generics.GenericAPIView):
    permission_classes = (AllowAny, )

    def post(self, request, *args, **kwargs):
        form_data = json.loads(request.body.decode())
        if len(form_data)>0:
            resp = {'form_data': 1}
        else:
            resp = {'form_data': 0}
        return JsonResponse(resp, status=status.HTTP_200_OK)


class GetGeoJson(generics.GenericAPIView):
    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):

        latitude = float(kwargs['latitude'])
        longitude = float(kwargs['longitude'])

        GeoJson = {
            "type": "FeatureCollection",
            "features": []
        }

        sensors = Sensor.objects.filter(latitude__lte=latitude+2, latitude__gte=latitude-2,
                              longitude__lte=longitude+2, longitude__gte=longitude-2)
        roads = []
        for sensor in sensors:
            data = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [ sensor.longitude, sensor.latitude, 0.0 ]
                }
            }
            GeoJson['features'].append(data)
            if not sensor.road in roads:
                roads.append(sensor.road)

        for road in roads:
            data = {
                "type": "line",
                "geometry": {
                    "type": "LineString",
                    "coordinates": [[ sensor.longitude, sensor.latitude ] for sensor in road.sensor_set.all()]
                }
            }
            GeoJson['features'].append(data)

        return JsonResponse(GeoJson, status=status.HTTP_200_OK)


class NewRoad(generics.GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        form_data = json.loads(request.body.decode())
        try:
            lane_count = form_data['lane_count']
            sensors = form_data['sensors']
        except:
            lane_count = None
            sensors = []

        try:
            username = form_data['username']
            password = form_data['password']
            two_way = form_data['2way']

            for sensor in sensors:
                if Sensor.objects.filter(latitude=sensor['latitude'],longitude=sensor['longitude']).exists():
                    raise Exception("Sensor already exists")

            road = Road.objects.create(
                username=username,
                password=password,
                lane_count=lane_count,
                two_way=two_way,
                first_name=' '.join(username.split(' ')[:-1]),
                last_name=username.split(' ')[-1]
            )
            road.set_password(password)
            road.save()

            login(request, road)

            for sensor in sensors:
                Sensor.objects.create(
                latitude=sensor['latitude'],
                longitude=sensor['longitude'],
                road=road
                )

            token, _ = Token.objects.get_or_create(user=road)

            response_data = {
                'token': token.key,
            }
            return JsonResponse(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            response_data = {'error_message': "Cannot sign you up due to " + str(e)}
            return JsonResponse(response_data, status=status.HTTP_400_BAD_REQUEST)


class GetData(generics.GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return JsonResponse({}, status=status.HTTP_200_OK)