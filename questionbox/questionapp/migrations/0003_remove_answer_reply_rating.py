# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionapp', '0002_auto_20150825_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='reply_rating',
        ),
    ]
