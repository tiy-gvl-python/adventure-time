# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionapp', '0006_auto_20150826_1117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='body',
            new_name='answer',
        ),
    ]
