from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('landing/', views.landing, name="landing"),
    path('harp/', views.harp, name="harp"),
    path('api/weather/', views.WeatherData.as_view(), name="weather"),
    path('api/get-geojson/', views.GetGeoJson.as_view(), name="get-geojson")
]
