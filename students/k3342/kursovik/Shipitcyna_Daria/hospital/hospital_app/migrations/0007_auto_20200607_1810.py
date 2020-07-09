# Generated by Django 3.0.6 on 2020-06-07 18:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0006_auto_20200607_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app_times',
            name='appointment_date',
        ),
        migrations.AddField(
            model_name='app_times',
            name='date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Дата приема'),
        ),
        migrations.AlterField(
            model_name='app_times',
            name='time_start',
            field=models.TimeField(default=datetime.datetime.now, verbose_name='Начало времени приема'),
        ),
        migrations.DeleteModel(
            name='App_dates',
        ),
    ]