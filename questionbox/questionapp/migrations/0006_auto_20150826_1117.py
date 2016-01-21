# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionapp', '0005_auto_20150826_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='tag',
            field=models.ManyToManyField(to='questionapp.Tag'),
        ),
    ]
