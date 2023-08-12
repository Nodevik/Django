from django.shortcuts import render
from django.core.cache import cache

# Create your views here.

# def home(request):
#     mv = cache.get('movie' , 'has_expired')
#     if mv == 'has_expired':
#         cache.set('movie' , 'avengers' , 30)
#         mv = cache.get('movie')
#     return render(request , 'home.html' , {'mv':mv})



# def home(request):
#     mv = cache.get_or_set('fess' , 4444 , 30 , version=2)
#     return render(request , 'home.html' , {'mv':mv})


# def home(request):
#     data = {'movie':"avengers" ,
#             'game':'pubg',
#             'food':'rasugulla'}
#     sv = cache.set_many(data , 30)
#     mv = cache.get_many(data)
#     return render(request , 'home.html' , {'mv':mv })


# def home(request):
#     cache.delete('movie')
#     return render(request , 'home.html')


# def home(request):                   #for this first needd to set 
#     cache.incr('roll' , delta=5)
#     print(cache.get('roll'))
#     return render(request , 'home.html')



def home(request):             #clear using termianal shell of django
    cache.clear()
    return render(request , 'home.html')