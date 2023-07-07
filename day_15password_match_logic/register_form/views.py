from django.shortcuts import render
from .forms import register
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
            print('name :' , name)
            print('password :' , password)
            print('rpassword :' , rpassword)
            return HttpResponseRedirect('/regi')
            # return render(request , 'thanks.html')
    else:
        fm = register()
    return render(request , 'index.html' ,{'form': fm})