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
        m1=getattr(self, 'everymin1')
        m2=getattr(self, 'everymin2')
        lastm=getattr(self, 'last_train')
        curtime = datetime.datetime.now().time()
        curhr = curtime.hour
        first_train = datetime.time(curhr, min(int(m1), int(m2)))
        sec_train = datetime.time(curhr, max(int(m1), int(m2)))
        nexthrTr =  datetime.time(curhr+1, min(int(m1), int(m2)))
        firstday_train =  datetime.datetime.strptime(getattr(self, 'first_train'), "%H:%M").time()
        lastday_train =  datetime.datetime.strptime(getattr(self, 'last_train'), "%H:%M").time()
        if curtime > lastday_train and curtime < firstday_train:
            return firstday_train
        elif curtime > first_train and curtime < sec_train:
            return sec_train
        elif curtime > sec_train and curtime < lastday_train:
            return nexthrTr
        else:
            return first_train

    class Meta:
        db_table = 'timetable'
        verbose_name = _('timetable to airport')

