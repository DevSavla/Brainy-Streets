from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('roads.urls')),
    path('api/weather/', views.WeatherData.as_view(), name="weather")
]
