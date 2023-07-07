from django.db import models

# Create your models here.
class student(models.Model):
    sid = models.IntegerField()
    sname = models.CharField(max_length=70)

    def __str__(self) -> str:
        return self.sname
    
    # def __str__(self) -> str:
    #     return str(self.sid)        #this is give a error if not convert in str