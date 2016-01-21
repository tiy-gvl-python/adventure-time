# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionapp', '0007_auto_20150826_1327'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AddField(
            model_name='tag',
            name='applies',
            field=models.BooleanField(default=False),
        ),
    ]
