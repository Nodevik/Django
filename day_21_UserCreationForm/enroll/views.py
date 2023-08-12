from django.shortcuts import render
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request , 'User sign up successfully')
            fm.save()
    else:
        fm = SignUpForm()
    return render(request , "sign_up.html" , {'form':fm})