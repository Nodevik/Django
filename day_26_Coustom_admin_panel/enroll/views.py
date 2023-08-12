from django.shortcuts import render , HttpResponseRedirect
from django.contrib import messages
from .forms import SignUpForm , UserProfileChange , AdminProfileChange
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm  , SetPasswordForm
from django.contrib.auth import authenticate  , logout  , update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User

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
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = AdminProfileChange(request.POST , instance=request.user)
                users = User.objects.all
            else:
                fm = UserProfileChange(request.POST , instance=request.user)
                users = None
            if fm.is_valid():
                messages.success(request , 'Profile Updated')
                fm.save()
        else:
            if request.user.is_superuser == True:
                fm = AdminProfileChange(instance=request.user)
                users = User.objects.all
            else:
                fm = UserProfileChange(instance=request.user)
                users = None
        return render(request , 'profile.html' , {'name':request.user , 'form':fm , 'users':users})
    else:
        return HttpResponseRedirect('/login/')




def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')




#change user pass with old password
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user , data = request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request , fm.user)
                return HttpResponseRedirect('/p/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request , 'changepass_with_old_pass.html' , {'form':fm})
    else:
        return HttpResponseRedirect('/signup/')
    


#change user pass without old password
def user_change_pass2(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = SetPasswordForm(user=request.user , data = request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request , fm.user)
                return HttpResponseRedirect('/p/')
        else:
            fm = SetPasswordForm(user=request.user)
        return render(request , 'changepass_without_old_pass.html' , {'form':fm})
    else:
        return HttpResponseRedirect('/signup/')
    


def user_det_admin(request,id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fm = AdminProfileChange(instance=pi)
        return render(request , 's_profile.html' , {'form':fm})
    else:
        return HttpResponseRedirect('/login/')