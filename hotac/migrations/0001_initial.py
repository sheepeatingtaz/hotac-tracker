# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 19:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('campaign', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnemySquadron',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('squadron_name', models.CharField(max_length=10)),
                ('vector', models.CharField(max_length=6)),
                ('arrival', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='EnemySquadronComposition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('players', models.IntegerField()),
                ('conditional_ps', models.IntegerField(blank=True, null=True)),
                ('elite', models.BooleanField(default=False)),
                ('enemy_squadron', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotac.EnemySquadron')),
                ('ship_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='campaign.ImperialShip')),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MissionArc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='mission',
            name='arc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotac.MissionArc'),
        ),
        migrations.AddField(
            model_name='enemysquadron',
            name='mission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotac.Mission'),
        ),
        migrations.AlterUniqueTogether(
            name='enemysquadroncomposition',
            unique_together=set([('enemy_squadron', 'players')]),
        ),
        migrations.AlterUniqueTogether(
            name='enemysquadron',
            unique_together=set([('squadron_name', 'mission')]),
        ),
    ]
