from django.conf.urls.defaults import *
from views import DailyViews

urlpatterns = patterns('',
    (r'^(?P<date>\d+-\d+)/$',DailyViews.monthly),
    (r'^(?P<date>\d+-\d+-\d+)/$',DailyViews.daily),
    (r'^$',DailyViews.latest),
)
