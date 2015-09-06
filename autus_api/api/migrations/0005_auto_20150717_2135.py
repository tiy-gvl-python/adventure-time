# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pandas as pd
from api.models import Respondent, Activity, Demographic

def load_demographic_data(apps, schema_editor):
    demographics = pd.read_csv('../atussum_2014/atussum_2014.dat')
    e = []
    for i in demographics:
        if i.isupper():
            e.append(i)
    demo = demographics[e + ['tucaseid']]

    for i in demo.iterrows():
        demobj = i[1]
        respondent = Respondent.objects.get(case_id=demobj.tucaseid)
        demobj = demobj.drop(['tucaseid', 'TEAGE', 'TESEX', 'TUFINLWGT', 'TEHRUSLT'])
        for e in demobj.index:
            Demographic.objects.create(respondent=respondent, code=e, value=demobj[e])






class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20150717_2134'),
    ]

    operations = [
        migrations.RunPython(load_demographic_data)
    ]
