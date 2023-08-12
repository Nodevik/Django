from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name'] = 'vikas'
    request.session.setdefault('age','16')
    return render(request, 'set_session.html')


def getsession(request):
    # name = request.session['name']
    name = request.session.get('name' , default='default')
    key = request.session.keys
    item = request.session.items
    return render(request, 'get_session.html' , {'name':name , 'keys':key ,'items':item })

def delsession(request):
    # if 'name' in request.session:
    #     del request.session['name']
        # return render(request, 'del_session.html')
    request.session.flush()                         #complete delete session
    return render(request, 'del_session.html')

    
