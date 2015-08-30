# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionapp', '0009_auto_20150826_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='reputation',
            field=models.IntegerField(default=0),
        ),
    ]
