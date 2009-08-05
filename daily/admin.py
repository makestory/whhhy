#coding=utf-8
from django.contrib import admin
from daily.models import Daily,Category
class DailyAdmin(admin.ModelAdmin):
    date_hierarchy='date'
    list_display = ('date','title','show','count','category')
    class Media:
        js =("/data/tiny_mce/tiny_mce.js","/data/textareas.js")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','describe')
admin.site.register(Daily,DailyAdmin)
admin.site.register(Category,CategoryAdmin)
