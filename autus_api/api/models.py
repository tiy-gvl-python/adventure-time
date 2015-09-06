from django.db import models
#  from jsonfield import JSONField

class Respondent(models.Model):
    case_id = models.BigIntegerField()  # TUCASEID
    age = models.IntegerField()  # TEAGE
    sex = models.IntegerField()  # TESEX
    weight = models.FloatField()  # TUFINLWGT
    hours_worked_per_week = models.BigIntegerField()  # TEHRUSLT

    def __str__(self):
        return str(self.case_id)

    #  json = JSONField()
            #####----xor----####
    """labor_status = models.IntegerField()  # TELFS
    labor_type = models.IntegerField()  # TRDPFTPT
    labor_partner = models.IntegerField()  # TESPEMPNOT
    labor_type_partner = models.IntegerField  # TRSPFTPT
    multiple_jobs = models.IntegerField()  # TEMJOT
    enrolled = models.IntegerField()  # TESCHENR
    _where = models.IntegerField()  # TESCHLVL
    household_children = models.IntegerField()  # TRCHILDNUM
    weekly_earnings = models.IntegerField()  # TRERNWA
    holiday = models.IntegerField()  # TRHOLIDAY
    partner_presence = models.IntegerField()  # TRSPPRES
    eldercare = models.IntegerField()  # TRTEC
    secondary_childcare = models.IntegerField()  # TRTHH
    youngest_child = models.IntegerField()  # TRYHHCHILD
    diary_day = models.IntegerField()  # TUDIARYDAY"""

    # this is dumb

class Activity(models.Model):
    respondent = models.ForeignKey(Respondent)
    cat_1 = models.CharField(max_length=2)
    cat_2 = models.CharField(max_length=2)
    cat_3 = models.CharField(max_length=2)
    minutes = models.IntegerField()

    def __str__(self):
        return str(self.cat_1) + str(self.cat_2) + str(self.cat_3)

class Demographic(models.Model):                # This way we can go through any number of demographic data
    respondent = models.ForeignKey(Respondent)  # Either we do this or we store it all in JSON
    code = models.CharField(max_length=20)
    value = models.FloatField()

    def __str__(self):
        return str(self.code)

