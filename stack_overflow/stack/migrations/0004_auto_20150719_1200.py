# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stack', '0003_auto_20150719_1156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='voter_pk',
            new_name='votee_pk',
        ),
    ]
