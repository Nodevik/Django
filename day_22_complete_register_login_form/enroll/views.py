from django.shortcuts import render , HttpResponseRedirect
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate  , logout 
from django.contrib.auth import login as auth_login

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


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request , data = request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                print(uname)
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    print(user)
                    auth_login(request,user)
                    return HttpResponseRedirect('/p/')
        else:
            fm = AuthenticationForm()
        return render(request , 'login.html' , {'form':fm})
    else:
        return HttpResponseRedirect('/p/')


def user_profile(request):
    if request.user.is_authenticated:
        return render(request , 'profile.html')
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')