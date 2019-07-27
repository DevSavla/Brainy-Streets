from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('landing/', views.landing, name="landing"),
    path('harp/', views.harp, name="harp")
]
