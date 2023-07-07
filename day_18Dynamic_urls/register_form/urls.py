from django.urls import path
from . import views
urlpatterns = [
    path('' , views.home , name="home"),
    path('regi/<int:id>' , views.thanks , name="thanks"),

]
