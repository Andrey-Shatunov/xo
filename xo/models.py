import datetime

from django.db import models
from django.utils import timezone
# Create your models here.

class Steps(models.Model):
    x=models.IntegerField(default=0)
    y=models.IntegerField(default=0)
    type=models.IntegerField(default=0)
