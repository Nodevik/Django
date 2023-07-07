from django.db import models

# Create your models here.
class student(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=70)