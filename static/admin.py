#coding=utf-8
from django.contrib import admin
from models import Wallpaper,File

class WapaperAdmin(admin.ModelAdmin):
    list_display = ('display','number')
    def display(self,request):
        return '<img src="%s" height="200px"/>' % (request.image.url)
    display.allow_tags = True

admin.site.register(Wallpaper,WapaperAdmin)
admin.site.register(File)
