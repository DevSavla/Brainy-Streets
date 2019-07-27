from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated, AllowAny

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
    permission_classes = (AllowAny, )

    def post(self, request, *args, **kwargs):
        return JsonResponse({}, status=status.HTTP_200_OK)

class GetGeoJson(generics.GenericAPIView):
    permission_classes = (AllowAny, )

    def get(self, request):
        GeoJson = {
            "type": "FeatureCollection",
            "features": []
        }

        all_data = [[ [72.828573, 18.931683], [72.838573, 18.931683], [72.838573, 18.941683] ]]

        for data in all_data:
            GeoJson['features'].append({ "type": "line", "geometry": { "type": "LineString", "coordinates": data } })

        return JsonResponse(GeoJson, status=status.HTTP_200_OK)