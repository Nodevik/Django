from django.shortcuts import render

# Create your views here.

def home(request):
    print('i am home')
    return render(request, 'home.html')


def about(request):
    print('i am about')
    return render(request, 'about.html')

