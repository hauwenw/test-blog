from django.conf.urls import url
from . import views
from datetime import datetime

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.PostView.as_view(), name='post'),
    url(r'^post/$', views.post_post, name='post-post'),
    url(r'^(?P<pk>[0-9]+)/comment$', views.post_comment, name='post-comment'),
]
