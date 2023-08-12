from django.urls import path
from . import views
from django.views.decorators.cache import cache_page             #config in settings.py 

urlpatterns = [
    path('set/', views.setsession , name='setsession'),
    # path('get/', cache_page(60)(views.getsession) , name='getsession'),       #store cache in db ,file,local likhne ka method 2 , change setting according to need
    path('get/', views.getsession , name='getsession'),
    path('del/', views.delsession , name='delsession'),

]
