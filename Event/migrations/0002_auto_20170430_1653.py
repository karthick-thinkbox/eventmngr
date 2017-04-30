# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-30 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='idcard_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='ticket_count',
            field=models.IntegerField(default=1, null=True),
        ),
    ]