from django.contrib import admin
from .models import Page , Like

# Register your models here.
@admin.register(Page)
class pageAdmin(admin.ModelAdmin):
    list_display = ['user','page_name', 'page_cat', 'page_publish_date']

    
@admin.register(Like)
class pageAdmin(admin.ModelAdmin):
    list_display = ['user','page_name', 'page_cat', 'page_publish_date']