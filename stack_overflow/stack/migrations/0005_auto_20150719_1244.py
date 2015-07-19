# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stack', '0004_auto_20150719_1200'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-score']},
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='points',
            new_name='score',
        ),
    ]
