from django.db import models
from .manager import CustomManager

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    mname = models.CharField(max_length=70)

    objects = models.Manager()              # by default
    vikas = models.Manager()                 #chnage manager name   {onjects == vikas} now
    Custom = CustomManager()              
