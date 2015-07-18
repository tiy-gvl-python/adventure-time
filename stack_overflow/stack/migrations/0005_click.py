# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stack', '0004_auto_20150718_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('answer', models.ForeignKey(to='stack.Answers', null=True)),
                ('profile', models.ForeignKey(to='stack.Profile', null=True)),
                ('question', models.ForeignKey(to='stack.Question', null=True)),
            ],
        ),
    ]
