# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('stack', '0002_auto_20150717_2249'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answers',
            options={'ordering': ['-score']},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-points']},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-score']},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['-score']},
        ),
        migrations.RemoveField(
            model_name='answers',
            name='user',
        ),
        migrations.AlterField(
            model_name='question',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from='title', editable=False),
        ),
    ]
