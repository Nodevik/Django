from django.shortcuts import render
from .models import student


# Create your views here.
def home(request):
    vv = student.objects.all()
    return render(request , 'index.html' , {"v":vv})