# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stack', '0002_auto_20150719_0257'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vote',
            name='is_answer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vote',
            name='is_question',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='vote',
            name='downvote',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='vote',
            name='upvote',
            field=models.BooleanField(default=False),
        ),
    ]
