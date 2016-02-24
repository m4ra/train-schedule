from django.conf.urls import url
from django.core.urlresolvers import reverse
from . import views
from .feeds import LatestEntriesFeed


urlpatterns = [
		    url(r'^$', views.index, name='index'),
		    url(r'^latest/feed/$', LatestEntriesFeed()),
		    ]
