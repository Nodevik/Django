from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=70)
    password = models.CharField(max_length=70)
    rpassword = models.CharField(max_length=70)
    