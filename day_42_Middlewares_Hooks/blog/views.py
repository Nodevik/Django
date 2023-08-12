from django.shortcuts import render , HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
def home(request):
    print('i am home view')
    return HttpResponse('this is home page')


def excp(request):
    print('i am exceptionn  view')
    a = 10/0
    return HttpResponse('this is exception page')

def user_info(request):
    print('i am user info view 3hool')
    context = {'name':'vikas'}
    return TemplateResponse(request, 'user.html', context)