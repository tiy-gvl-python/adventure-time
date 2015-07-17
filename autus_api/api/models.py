from django.db import models

"""class Respondent(models.Model):
    case_id = models.IntegerField()  # TUCASEID
    age = models.IntegerField()  # TEAGE
    sex = models.IntegerField()  # TEAGE
    weight = models.IntegerField()  # TUFINLWGT
    hours_worked_per_week = models.IntegerField()  # TEHRUSLT
            #####----xor----####
    labor_status = models.IntegerField()  # TELFS
    labor_type = models.IntegerField()  # TRDPFTPT
    labor_partner = models.IntegerField()  # TESPEMPNOT
    labor_type_partner = models.IntegerField  # TRSPFTPT
    mulitple_jobs = models.IntegerField()  # TEMJOT
    enrolled = models.IntegerField()  # TESCHENR
    _where = models.IntegerField()  # TESCHLVL
    household_children = models.IntegerField()  # TRCHILDNUM
    weekly_earnings = models.IntegerField()  # TRERNWA
    holiday = models.IntegerField()  # TRHOLIDAY
    partner_presence = models.IntegerField()  # TRSPPRES
    eldercare = models.IntegerField()  # TRTEC
    secondary_childcare = models.IntegerField()  # TRTHH
    youngest_child = models.IntegerField()  # TRYHHCHILD
    diary_day = models.IntegerField()  # TUDIARYDAY

    # this is dumb

class Activity(models.Model):
    respondent = models.ForeignKey(Respondent)
    cat_1 = models.CharField(max_length=2)
    cat_2 = models.CharField(max_length=2)
    cat_3 = models.CharField(max_length=2)
    minutes = models.IntegerField()


class Demographic(models.Model):                # This way we can go through any number of demographic data
    respondent = models.ForeignKey(Respondent)  # Either we do this or we store it all in JSON
    code = models.CharField(max_length=20)
    value = models.IntegerField()"""