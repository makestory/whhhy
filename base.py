#!/usr/bin/env python
from daily.models import Daily
from static.models import Wallpaper


def getwallpaper():
    return Wallpaper.objects.all()

class BaseView(object):
    def __init__(self):
        self.para = self.getpara()
    @staticmethod
    def getpara(para=None):
        para= {
        'years':Daily.objects.filter(show=True).dates('date','year'),
        'months':Daily.objects.filter(show=True).dates('date','month','DESC'),
        'days':Daily.objects.filter(show=True).dates('date','day','DESC'),
        'wallpaper':getwallpaper()}
        return para
