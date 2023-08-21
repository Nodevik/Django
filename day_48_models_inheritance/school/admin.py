from django.contrib import admin
from .models import brother , sister ,ExamCenter , Student , Village , Kas
# Register your models here.


#=======================================  Abstract class inheritance =====================
@admin.register(brother)
class brotherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
@admin.register(sister)
class sisterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']



#=======================================  Multi Table inheritance =====================
@admin.register(ExamCenter)
class centerAdmin(admin.ModelAdmin):
    list_display = ['id', 'centerName', 'city']
    
@admin.register(Student)
class stuAdmin(admin.ModelAdmin):
    list_display = ['id', 'roll']


#=======================================  Proxy Model inheritance =====================
@admin.register(Village)
class VillageAdmin(admin.ModelAdmin):
    list_display = [ 'id','centerName2', 'city2']
    
@admin.register(Kas)
class KasAdmin(admin.ModelAdmin):
    list_display = [ 'id']