from django.shortcuts import render
from .forms import register
from .models import User
from django.http import HttpResponseRedirect

# Create your views here.
def thanks(request):
    return render(request , 'thanks.html')


def home(request):
    if request.method == 'POST':
        fm = register(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            password = fm.cleaned_data['password']
            rpassword = fm.cleaned_data['rpassword']
            obj = User(name=name , password=password , rpassword=rpassword)
            obj.save()
            return HttpResponseRedirect('/regi')
            # return render(request , 'thanks.html')
    else:
        fm = register()
    return render(request , 'index.html' ,{'form': fm})