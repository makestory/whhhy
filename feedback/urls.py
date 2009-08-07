from django.conf.urls.defaults import *
from views import FeedbackViews

urlpatterns = patterns('',
    (r'^$',FeedbackViews.feedback),
    (r'^ajax/$','feedback.views.ajax'),
    (r'^delete/$','feedback.views.delete'),
)
