#coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from base import BaseView
from daily.models import Daily

class HomeView(BaseView):
    @classmethod
    def homepage(cls,request):
        para=BaseView().para
        return render_to_response('base.html',para)
    
    @classmethod
    def about(cls,request):
        para=BaseView().para
        return render_to_response('about.html',para)
    

def rss(request):
    dailys=Daily.objects.filter(show=True).all()[:10]
    return render_to_response('rss.xml',{'dailys':dailys})
