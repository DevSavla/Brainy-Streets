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