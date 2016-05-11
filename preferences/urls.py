from django.conf.urls import url
from . import views

app_name = 'profile'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.Profile.as_view(), name='profile'),
    url(r'^(?P<pk>[0-9]+)/update_time/$', views.update_time, name='update_time'),
    url(r'^(?P<pk>[0-9]+)/update_subreddits/$', views.update_subreddits, name='update_subreddits'),
    url(r'^(?P<pk>[0-9]+)/delete_subreddit/$', views.delete_subreddit, name='delete_subreddit'),
]
