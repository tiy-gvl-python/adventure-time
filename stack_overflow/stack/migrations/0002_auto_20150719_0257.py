# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='votes',
            field=models.ManyToManyField(to='stack.Vote'),
        ),
        migrations.AddField(
            model_name='question',
            name='votes',
            field=models.ManyToManyField(to='stack.Vote'),
        ),
        migrations.AddField(
            model_name='vote',
            name='voter',
            field=models.ForeignKey(to='stack.Profile', default=None),
        ),
        migrations.AddField(
            model_name='vote',
            name='voter_pk',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=140),
        ),
    ]
