# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionapp', '0003_remove_answer_reply_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={},
        ),
    ]
