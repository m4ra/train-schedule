from django.db import models
from django.utils.translation import ugettext_lazy as _
import datetime

# Create your models here.

class Timetable(models.Model):
    station = models.CharField(_('station'), max_length=200, blank=True)
    first_train = models.CharField(_('first_train'), max_length=200, blank=True)
    sec_train = models.CharField(_('second train'), max_length=200, blank=True)

    min1 = models.DateTimeField(_('minutes1'), blank=True)
    min2 = models.DateTimeField(_('minutes2'), blank=True)
    everymin1 = models.TextField(_('every minutes1'), max_length=200, blank=True)
    everymin2 = models.TextField(_('every minutes2'), max_length=200, blank=True)
    last_train = models.TextField(_('last train'), max_length=200, blank=True)
    duration = models.TextField(_('travel duration'), max_length=200, blank=True)

    def train_per_hour(self):
        self.trains_now = {} 
        m1=getattr(self, 'everymin1')
        m2=getattr(self, 'everymin2')
        lastm=getattr(self, 'last_train')
        curtime = datetime.datetime.now().time()
        curhr = curtime.hour
        first_train = datetime.time(curhr, min(int(m1), int(m2)))
        self.trains_now['first_train'] = first_train
        sec_train = datetime.time(curhr, max(int(m1), int(m2)))
        self.trains_now['sec_train'] = sec_train
        nexthrTr =  datetime.time(curhr+1, min(int(m1), int(m2)))
        firstdayTr =  datetime.datetime.strptime(getattr(self, 'first_train'), "%H:%M").time()
        lastdayTr =  datetime.datetime.strptime(getattr(self, 'last_train'), "%H:%M").time()
        if curtime > lastdayTr and curtime < firstdayTr:
            firstdayTr
        elif curtime > first_train and curtime < sec_train:
            return sec_train
        elif curtime > sec_train and curtime < lastdayTr:
            return nexthrTr
        else:
            return first_train

    class Meta:
        db_table = 'timetable'
        verbose_name = _('timetable to airport')

