# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('cat_1', models.CharField(max_length=2)),
                ('cat_2', models.CharField(max_length=2)),
                ('cat_3', models.CharField(max_length=2)),
                ('minutes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Demographic',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('code', models.CharField(max_length=20)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Respondent',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('case_id', models.IntegerField()),
                ('age', models.IntegerField()),
                ('sex', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('hours_worked_per_week', models.IntegerField()),
                ('labor_status', models.IntegerField()),
                ('labor_type', models.IntegerField()),
                ('labor_partner', models.IntegerField()),
                ('mulitple_jobs', models.IntegerField()),
                ('enrolled', models.IntegerField()),
                ('_where', models.IntegerField()),
                ('household_children', models.IntegerField()),
                ('weekly_earnings', models.IntegerField()),
                ('holiday', models.IntegerField()),
                ('partner_presence', models.IntegerField()),
                ('eldercare', models.IntegerField()),
                ('secondary_childcare', models.IntegerField()),
                ('youngest_child', models.IntegerField()),
                ('diary_day', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='demographic',
            name='respondent',
            field=models.ForeignKey(to='api.Respondent'),
        ),
        migrations.AddField(
            model_name='activity',
            name='respondent',
            field=models.ForeignKey(to='api.Respondent'),
        ),
    ]
