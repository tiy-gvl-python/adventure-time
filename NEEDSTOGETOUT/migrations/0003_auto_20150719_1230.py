# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NEEDSTOGETOUT', '0002_auto_20150718_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversationthread',
            name='updated',
            field=models.DateTimeField(default=1, auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postreply',
            name='updated',
            field=models.DateTimeField(default=1, auto_now=True),
            preserve_default=False,
        ),
    ]
