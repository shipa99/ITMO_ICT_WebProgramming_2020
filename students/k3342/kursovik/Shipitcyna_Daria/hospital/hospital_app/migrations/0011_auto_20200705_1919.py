# Generated by Django 3.0.6 on 2020-07-05 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0010_auto_20200628_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.CharField(default='не указана', max_length=50, verbose_name='Адрес электронной почты'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone',
            field=models.CharField(default='не указан', max_length=11, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='sex',
            field=models.CharField(choices=[('мужской', 'мужской'), ('женский', 'женский')], max_length=7, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='type',
            field=models.CharField(choices=[('гинеколог', 'гинеколог'), ('окулист', 'окулист'), ('терапевт', 'терапевт'), ('кардиолог', 'кардиолог')], max_length=11, verbose_name='Специализация врача'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='work_times',
            field=models.ManyToManyField(blank=True, default=[], through='hospital_app.Schedule', to='hospital_app.App_times'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.CharField(default='не указана', max_length=50, verbose_name='Адрес электронной почты'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(default='не указан', max_length=11, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.CharField(choices=[('мужской', 'мужской'), ('женский', 'женский')], max_length=7, verbose_name='Пол'),
        ),
    ]
