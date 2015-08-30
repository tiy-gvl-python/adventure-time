# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionapp', '0010_question_reputation'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='reputation',
            field=models.IntegerField(default=0),
        ),
    ]
