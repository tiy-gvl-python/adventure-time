# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='administrator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tag',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
