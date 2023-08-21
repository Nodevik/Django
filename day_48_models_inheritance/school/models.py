from django.db import models

# Create your models here.



#=======================================  Abstract class inheritance =====================
class Common(models.Model):
    name = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50)
    class Meta:
        abstract = True

class brother(Common):
    sub = models.CharField(max_length=50)

class sister(Common):
    course = models.CharField(max_length=50) 






#=======================================  Multi Table inheritance =====================
class ExamCenter(models.Model):
    centerName = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

class Student(ExamCenter):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()




#=======================================  Proxy Model inheritance =====================
class Village(models.Model):
    centerName2 = models.CharField(max_length=50)
    city2 = models.CharField(max_length=50)

class Kas(Village):
    class Meta:
        proxy = True