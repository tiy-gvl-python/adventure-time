# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stack', '0003_auto_20150718_0508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answers',
        ),
        migrations.AddField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(default=1, to='stack.Question'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answers',
            name='user',
            field=models.ForeignKey(default=1, to='stack.Profile'),
            preserve_default=False,
        ),
    ]
