# Generated by Django 3.0.6 on 2020-06-28 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0009_auto_20200618_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='type',
            field=models.CharField(choices=[('GYN', 'гинеколог'), ('OK', 'окулист'), ('TER', 'терапевт'), ('CAR', 'кадиолог')], default=1, max_length=3, verbose_name='Специализация врача'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='paid',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='service',
            field=models.ManyToManyField(blank=True, to='hospital_app.PriceList'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='sex',
            field=models.CharField(choices=[('male', 'мужской'), ('female', 'женский')], max_length=6, verbose_name='Пол'),
        ),
    ]
