from .  import views
from django.urls import path

urlpatterns = [
    path('signup/' , views.sign_up , name='sign_up'),
    path('login/' , views.user_login , name='user_login'),
    path('p/' , views.user_profile , name='user_profile'),
    path('logout/' , views.user_logout , name='user_logout'),
    path('changepass/' , views.user_change_pass , name='changepass'),
    path('changepass2/' , views.user_change_pass2 , name='changepass2'),

]
