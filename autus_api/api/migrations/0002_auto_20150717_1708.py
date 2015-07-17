# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respondent',
            name='_where',
        ),
        migrations.RemoveField(
            model_name='respondent',
            name='diary_day',
        ),
        migrations.RemoveField(
            model_name='respondent',
            name='eldercare',
        ),
        migrations.RemoveField(
            model_name='respondent',
            name='enrolled',
        ),
        migrations.RemoveField(
            model_name='respondent',
            name='holiday',
        ),
        migrations.RemoveField(
            model_name='respondent',
            name='household_children',
        ),
        migrations.RemoveField(
            model_name='respondent',
            name='labor_partner',
        ),
        migrations.RemoveField(
            model_name='respondent',
            name='labor_status',
        ),
        migrations.RemoveField(
            model_name='respondent',
            name='labor_type',
        ),
        migrations.RemoveField(
            model_name='respondent',
            name='mulitple_jobs',
        ),
        migrations.RemoveField(
            model_name='respondent',
            name='partner_presence',
        ),
        migrations.RemoveField(
            model_name='respondent',
            name='secondary_childcare',
        ),
        migrations.RemoveField(
            model_name='respondent',
            name='weekly_earnings',
        ),
        migrations.RemoveField(
            model_name='respondent',
            name='youngest_child',
        ),
        migrations.AlterField(
            model_name='respondent',
            name='weight',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='respondent',
            name='weight',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='respondent',
            name='case_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='respondent',
            name='hours_worked_per_week',
            field=models.BigIntegerField(),
        ),
    ]
