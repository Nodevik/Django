from django.shortcuts import render
from django.contrib import messages




def home(request):
    messages.add_message(request , messages.INFO , 'this is info')
    print(messages.get_level(request))
    messages.success(request , 'this is Success')
    print(messages.set_level(request , messages.DEBUG))
    messages.debug(request , 'this is debug')

    return render(request , 'index.html')