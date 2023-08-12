from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name'] = 'vikas'
    # request.session.set_expiry(600)          #set expiry of session
    request.session.set_test_cookie()         #test cookie set
    return render(request, 'set_session.html')


def getsession(request):
    if 'name' in request.session:
        name = request.session['name']
        request.session.modified = True   #if its true session automatically modify when use interect with web page
        request.session.test_cookie_worked()      # test cookie get return true false
    return render(request, 'get_session.html' , {'name':name})

def delsession(request):
    request.session.flush()
    request.session.clear_expired()     #help to clear database form expired session data
    request.session.delete_test_cookie()          # test cookie delete
    return render(request, 'del_session.html')

    
