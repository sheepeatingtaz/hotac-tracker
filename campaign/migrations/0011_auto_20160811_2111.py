# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-11 20:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0010_squadron_archived'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='squadronmember',
            options={'ordering': ('-admin', 'pilot_owner')},
        ),
        migrations.AddField(
            model_name='campaign',
            name='sqaudron',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='campaign.Squadron'),
            preserve_default=False,
        ),
    ]
