from django.shortcuts import render

# Create your views here.
def landing(requets):
    return render(requets , 'index.html')