from django.shortcuts import render
from django.views.decorators.cache import cache_page

# Create your views here.
@cache_page(60)                                           #store cache in db likhne ka method 1
def setsession(request):
    request.session['name'] = 'vikas'
    # request.session.set_expiry(600)          #set expiry of session
    request.session.set_test_cookie()         #test cookie set
    return render(request, 'set_session.html')


def getsession(request):
    name = request.session['name']
    return render(request, 'get_session.html' , {'name':name})

def delsession(request):
    request.session.flush()
    request.session.clear_expired()     #help to clear database form expired session data
    return render(request, 'del_session.html')

    
