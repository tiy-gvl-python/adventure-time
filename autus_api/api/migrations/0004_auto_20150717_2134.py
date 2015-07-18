# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150717_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demographic',
            name='value',
            field=models.FloatField(),
        ),
    ]
