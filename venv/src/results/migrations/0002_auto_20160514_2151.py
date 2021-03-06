# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-14 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footballteam',
            name='draws_away',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='footballteam',
            name='draws_home',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='footballteam',
            name='draws_total',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='footballteam',
            name='games_away',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='footballteam',
            name='games_home',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='footballteam',
            name='games_total',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='footballteam',
            name='goal_diff',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='footballteam',
            name='goals_against_away',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='footballteam',
            name='goals_against_home',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='footballteam',
            name='goals_against_total',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='footballteam',
            name='goals_for_away',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='footballteam',
            name='goals_for_home',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='footballteam',
            name='goals_for_total',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='footballteam',
            name='losses_away',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='footballteam',
            name='losses_home',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='footballteam',
            name='losses_total',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='footballteam',
            name='points_away',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='footballteam',
            name='points_home',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='footballteam',
            name='points_total',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='footballteam',
            name='wins_away',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='footballteam',
            name='wins_home',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='footballteam',
            name='wins_total',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
