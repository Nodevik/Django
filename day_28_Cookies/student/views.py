from django.shortcuts import render
from datetime import datetime , timedelta

# Create your views here.
def setcookie(request):
    response = render(request,'set_cookie.html')
    # response.set_cookie('name','vikas' , expires=datetime.utcnow()+timedelta(days=2))
    # response.set_cookie('name','vikas', max_age=120)
    response.set_signed_cookie('name','vikas' , salt='nm' , expires=datetime.utcnow()+timedelta(days=2))
    return response


def getcookie(request):
    # name = request.COOKIES['name']           #cookie is not set then this through error
    # name = request.COOKIES.get('name')          #cookie is not set then this not through error and return None
    # name = request.COOKIES.get('name' , 'guest')          #cookie is not set then this not through error and return default value
    name = request.get_signed_cookie('name' , default='Guest' , salt='nm')          #getting signed cookie here
    return render(request , 'get_cookie.html' , {'name':name})


def delcookie(request):
    response = render(request , 'del_cookie.html')
    response.delete_cookie('name')
    return response