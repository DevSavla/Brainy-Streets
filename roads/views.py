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

def landing(request):
    return  render(request, 'landing.html')

def harp(request):
    return render(request, 'harp.html')

class WeatherData(generics.GenericAPIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        return JsonResponse({}, status=status.HTTP_200_OK)


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
        try:
            lane_count = request.POST.get('lane_count')
            sensors = request.POST.get('sensors')
        except:
            lane_count = None
            sensors = []

        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            two_way = request.POST.get('2way')

            for sensor in sensors:
                Sensor.objects.create(
                    latitude=sensor['latitude'],
                    longitude=sensor['longitude']
                )

            road = Road.objects.create(
                username=username,
                password=password,
                lane_count=lane_count,
                two_way=two_way,
                f_name=username.split(' ')[:-1].join(),
                l_name=username.split(' ')[-1]
            )
            road.set_password(password)
            road.save()

            login(request, road)

            token, _ = Token.objects.get_or_create(user=road)

            response_data = {
                'token': token.key,
            }
            return JsonResponse(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            response_data = {'error_message': "Cannot sign you up due to " + str(e)}
            return JsonResponse(response_data, status=status.HTTP_400_BAD_REQUEST)
