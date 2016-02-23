from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Timetable(models.Model):
    station = models.CharField(_('station'), max_length=200, blank=True)
    min1 = models.DateTimeField(_('minutes1'), blank=True)
    min2 = models.DateTimeField(_('minutes2'), blank=True)

    class Meta:
        db_table = 'timetable'
        verbose_name = _('timetable to airport')

