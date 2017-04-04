import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class Room(models.Model):
    room_name = models.CharField(max_length=200,default="")
    user_one = models.CharField(max_length=200,default="0")
    user_two = models.CharField(max_length=200,default="0")
    def __str__(self):
        return self.room_name

class Steps(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE,default="")
    player = models.CharField(max_length=200,default="")
    x=models.IntegerField(default=0)
    y=models.IntegerField(default=0)
    type=models.IntegerField(default=0)

class Statistics(models.Model):
    player = models.CharField(max_length=200,unique=True)
    win=models.IntegerField(default=0)
    loose = models.IntegerField(default=0)
