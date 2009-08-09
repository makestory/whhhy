from django.conf.urls.defaults import *
from views import FeedbackViews,ajax,more,delete

urlpatterns = patterns('',
    (r'^$',FeedbackViews.feedback),
    (r'^ajax/$',ajax),
    (r'^delete/$',delete),
    (r'^more/$',more),
)
