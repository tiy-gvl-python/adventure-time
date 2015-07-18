# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pandas as pd
from api.models import Respondent, Activity, Demographic

def load_activity_data(apps, schema_editor):
    activity = pd.read_csv('../atussum_2014/atussum_2014.dat')
    emp_list = []
    for col in activity:
        if col.islower():
            emp_list.append(col)
    activate = activity[emp_list]
    for row in activate.iterrows():
        actobj = row[1]
        respondent = Respondent.objects.get(case_id=actobj.tucaseid)
        actobj = actobj.drop('tucaseid')
        for col_name in actobj.index:
            a = col_name[1:3]
            b = col_name[3:5]
            c = col_name[5:7]
            Activity.objects.create(respondent=respondent, cat_1=a, cat_2=b, cat_3=c, minutes=actobj[col_name])




class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20150718_0026'),
    ]

    operations = [
        migrations.RunPython(load_activity_data)
    ]
