from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.


class Road(AbstractUser):
    lane_count = models.PositiveSmallIntegerField(default=None, null=True)
    two_way = models.BooleanField()


class Sensor(models.Model):
    latitude = models.DecimalField(max_digits=13, decimal_places=8)
    longitude = models.DecimalField(max_digits=13, decimal_places=8)
    road = models.ForeignKey(Road, on_delete=models.CASCADE)

    def __str__(self):

        if self.latitude >= 0:
            latitude_direction = " N "
        else:
            latitude_direction = " S "


        if self.longitude >= 0:
            longitude_direction = " E"
        else:
            longitude_direction = " W"

        return str(self.latitude) + latitude_direction + self(self.longitude) + longitude_direction


# class Data(models.Model):
#     created = models.DateTimeField(auto_now=True)
