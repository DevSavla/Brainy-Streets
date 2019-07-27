from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')

def landing(request):
    return  render(request, 'landing.html')

def harp(request):
    return render(request, 'harp.html')