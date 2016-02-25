from django.shortcuts import render
from .models import Timetable
import datetime
import pytz
from django.utils import timezone
from django.http import HttpResponse
from django.template import RequestContext, loader
import feedparser
 
def feeds(request):
    template = loader.get_template('trains/feeds.html')
    feed = feedparser.parse('http://www.meteo.gr/rss/news.cfm')
    title =feed['entries'][1].title
    context = {
	'feed':feed,
	'title':title
        }
    return HttpResponse(template.render(context, request))


def index(request):
    timetables = Timetable.objects.all()
    cur_time=datetime.datetime.now().time()
    template = loader.get_template('trains/index.html')
    if request.method == "POST" and request.POST:
        query = request.POST['q']
        cur_hour=cur_time.hour
        cur_station = Timetable.objects.filter(station=query).first()
        next_station = Timetable.objects.filter(id=cur_station.id+1).first()
        prev_id=cur_station.id -1
        prev_station = Timetable.objects.filter(id=prev_id).first()

        #Get the min and the max minutes in the hour of the train
        # this is necessary because the timetable hasn't indexed the minutes by time order 
        min_everymin = min(int(cur_station.everymin1), int(cur_station.everymin2))
        max_everymin = max(int(cur_station.everymin1), int(cur_station.everymin2))
        min_everyminNext = min(int(next_station.everymin1), int(next_station.everymin2))
        max_everyminNext = max(int(next_station.everymin1), int(next_station.everymin2))
        min_everyminPrev = min(int(prev_station.everymin1), int(prev_station.everymin2))
        max_everyminPrev = max(int(prev_station.everymin1), int(prev_station.everymin2))
        
        #get train times when current time is within the stations' time
        train_pass1 = datetime.time(cur_hour, min_everymin)
        train_pass2 = datetime.time(cur_hour, max_everymin)

        train_next1 = datetime.time(cur_hour, min_everyminNext)
        train_next2 = datetime.time(cur_hour, max_everyminNext)

        train_prev1 = datetime.time(cur_hour, min_everyminPrev)
        train_prev2 = datetime.time(cur_hour, max_everyminPrev)

        #get the next hour train in case current time is closer to next hour train 
        if cur_hour < 5:  #if current time is after 00:00, need the first trains which start after 05:00
            ft_hour = cur_station.first_train.split(':')[0]
            ft_min = cur_station.first_train.split(':')[1]
            ft_hourN = next_station.first_train.split(':')[0]
            ft_minN = next_station.first_train.split(':')[1]
            ft_hourP = prev_station.first_train.split(':')[0]
            ft_minP = prev_station.first_train.split(':')[1]
            next_hourTrain = datetime.time(int(ft_hour), int(ft_min))
            next_hourTrainNext = datetime.time(int(ft_hourN), int(ft_minN))
            next_hourTrainPrev = datetime.time(int(ft_hourP), int(ft_minP))

        else: #get the next hour trains instead  
            next_hourTrain = datetime.time(cur_hour+1, min_everymin)
            next_hourTrainNext = datetime.time(cur_hour+1, min_everyminNext)
            next_hourTrainPrev = datetime.time(cur_hour+1, min_everyminPrev)

        context = {
            'timetables':timetables,
            'station':cur_station.station,
            'next_station':next_station.station,
            'prev_station':prev_station.station,
            'time':cur_time,
            'train_pass1': train_pass1,
            'train_pass2': train_pass2,
            'train_next1': train_next1,
            'train_next2': train_next2,
            'train_prev1': train_prev1,
            'train_prev2': train_prev2,
            'next_hourTrain': next_hourTrain, 
            'next_hourTrainNext': next_hourTrainNext,
            'next_hourTrainPrev': next_hourTrainPrev
            }
    else:
        context =  {
            'timetables':timetables,
            'time':cur_time,
            }
    return HttpResponse(template.render(context, request))



