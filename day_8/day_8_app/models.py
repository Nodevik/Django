from django.db import models

# Create your models here.
class student(models.Model):
    stuname = models.CharField(max_length=54)
    fname = models.CharField(max_length=54)