# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-10 06:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FarmData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=256)),
                ('village', models.CharField(max_length=256)),
                ('crop_grown', models.CharField(max_length=256)),
                ('sowing_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FarmerData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('phone_number', models.CharField(max_length=12)),
                ('language', models.CharField(choices=[('English', 'English'), ('Hindi', 'Hindi')], default='English', max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days_after_sowing', models.DateField(null=True)),
                ('fertilizer', models.CharField(max_length=256)),
                ('quantity', models.IntegerField()),
                ('quantity_unit', models.CharField(choices=[('ton', 'ton'), ('kg', 'kg'), ('g (Solid)', 'g'), ('L (Liquid)', 'L'), ('mL (Liquid)', 'mL')], default='ton', max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
