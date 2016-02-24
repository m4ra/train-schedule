from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Timetable(models.Model):
    station = models.CharField(_('station'), max_length=200, blank=True)
    first_train = models.CharField(_('first_train'), max_length=200, blank=True)
    sec_train = models.CharField(_('second train'), max_length=200, blank=True)

    min1 = models.DateTimeField(_('minutes1'), blank=True)
    min2 = models.DateTimeField(_('minutes2'), blank=True)
    everymin1 = models.CharField(_('every minutes1'), max_length=200, blank=True)
    everymin2 = models.CharField(_('every minutes2'), max_length=200, blank=True)
    last_train = models.CharField(_('last train'), max_length=200, blank=True)
    duration = models.CharField(_('travel duration'), max_length=200, blank=True)

    class Meta:
        db_table = 'timetable'
        verbose_name = _('timetable to airport')

