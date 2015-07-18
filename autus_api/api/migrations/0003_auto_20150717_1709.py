# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pandas as pd
from api.models import Respondent, Activity, Demographic


def load_respondent_data(apps, schema_editor):
    responder = pd.read_csv('../atussum_2014/atussum_2014.dat')
    respy = responder[['tucaseid', 'TEAGE', 'TESEX', 'TUFINLWGT', 'TEHRUSLT']]



    for row in respy.iterrows():
        resobj = row[1]
        Respondent.objects.create(case_id=resobj.tucaseid, age=resobj.TEAGE, sex=resobj.TESEX,
                                  weight=resobj.TUFINLWGT, hours_worked_per_week=resobj.TEHRUSLT)


class Migration(migrations.Migration):


    dependencies = [
        ('api', '0002_auto_20150717_1708'),
    ]

    operations = [
        migrations.RunPython(load_respondent_data)
    ]
