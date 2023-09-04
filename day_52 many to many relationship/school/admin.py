from django.contrib import admin
from .models import song
# Register your models here.
@admin.register(song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['song_name','song_dur','write']