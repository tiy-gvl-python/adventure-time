# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('questionapp', '0004_auto_20150825_1302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='thread',
            new_name='question',
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='question',
            name='tag',
        ),
        migrations.AddField(
            model_name='question',
            name='tag',
            field=models.ManyToManyField(null=True, to='questionapp.Tag'),
        ),
        migrations.AlterField(
            model_name='question',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
