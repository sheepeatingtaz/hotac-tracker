# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0006_auto_20160726_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaignmission',
            name='turn',
            field=models.IntegerField(default=0),
        ),
    ]
