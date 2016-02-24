# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 20:09
from __future__ import unicode_literals

from django.db import migrations, models
import datetime

data_dict = {
                'AGHIA MARINA'  : [0, '05:30', '05:56', '26', '56', '22:56', '48'],
                'EGALEO': [1, '05:31', '05:58', '28', '58', '22:58', '46'],
                'ELEONAS'  : [2, '05:33', '05:59', '29', '59', '22:59', '45'],
                'KERAMEIKOS'  : [3, '05:35', '06:02', '32', '02', '23:02', '42'],
                'MONASTIRAKI' : [4, '05:38', '06:04', '34', '04', '23:04', '40'],
                'SYNTAGMA' : [5, '05:40', '06:06', '36', '06', '23:06', '38'],
                'EVANGELISMOS' : [6, '05:41', '06:08', '38', '08', '23:08', '36'],
                'MEGARO MOUSSIKIS' : [7, '05:43', '06:09', '39', '09', '23:09', '34'],
                'AMBELOKIPI' : [8, '05:44', '06:11', '41', '11', '23:11', '32'],
		'PALLINI' : [9, '06:04', '06:30', '00', '30', '23:30', '14'],
		'PEANIA-KANTZA' : [10, '06:06', '06:32', '02', '32', '23:32', '12'],
		'KOROPI' : [11, '06:12', '06:38', '08', '38', '23:38', '6'],
		'AIRPORT' :[12, '06:18', '06:44', '14', '44', '23:44', '0']
            }

def forwards_func(apps, schema_editor):
    Timetable = apps.get_model("trains", "Timetable")
    db_alias = schema_editor.connection.alias
    for i in data_dict:
        Timetable.objects.using(db_alias).bulk_create([
        Timetable(id=data_dict[i][0], station=i, first_train=data_dict[i][1], sec_train=data_dict[i][2], everymin1=data_dict[i][3], everymin2=data_dict[i][4], min1=datetime.datetime.now(), min2=datetime.datetime.now(), last_train=data_dict[i][5], duration=data_dict[i][6]),
    ])

def reverse_func(apps, schema_editor):
    # forwards_func() creates two Timetable instances,
    # so reverse_func() should delete them.
    Timetable = apps.get_model("trains", "Timetable")
    db_alias = schema_editor.connection.alias
    for i in data_dict:
        Timetable.objects.using(db_alias).filter(station=i).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('trains', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='duration',
            field=models.CharField(blank=True, max_length=200, verbose_name='travel duration'),
        ),
        migrations.AddField(
            model_name='timetable',
            name='first_train',
            field=models.CharField(blank=True, max_length=200, verbose_name='first_train'),
        ),
        migrations.AddField(
            model_name='timetable',
            name='last_train',
            field=models.CharField(blank=True, max_length=200, verbose_name='last train'),
        ),
        migrations.AddField(
            model_name='timetable',
            name='sec_train',
            field=models.CharField(blank=True, max_length=200, verbose_name='second train'),
        ),
        migrations.AddField(
            model_name='timetable',
            name='everymin1',
            field=models.CharField(blank=True, max_length=200, verbose_name='second train'),
        ),
        migrations.AddField(
            model_name='timetable',
            name='everymin2',
            field=models.CharField(blank=True, max_length=200, verbose_name='second train'),
        ),
        migrations.RunPython(forwards_func, reverse_func),
    ]