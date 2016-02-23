from django.shortcuts import render
from .models import Timetable
import datetime
import pytz
from django.utils import timezone
#from django.template import RequestContext
from django.http import HttpResponse
from django.template import loader
import feedparser
 
#def feeds(request):
#    feed = feedparser.parse(
#    template = loader.get_template('trains/index.html')


def index(request):
    timetables = Timetable.objects.all()
    cur_time=datetime.datetime.now().time
    feed = feedparser.parse('http://www.meteo.gr/rss/news.cfm')
    title =feed['entries'][1].title
    template = loader.get_template('trains/index.html')
    context = {
        'timetables':timetables,
        'time':cur_time,
	'feed':feed,
	'title':title
        }
    return HttpResponse(template.render(context, request))



# Create your views here.
