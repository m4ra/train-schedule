from django.contrib import admin
from .models import Timetable

@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    #form=TimetableForm
    list_display = ['station']

# Register your models here.
