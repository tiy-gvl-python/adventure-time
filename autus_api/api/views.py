from django.http import JsonResponse
from django.shortcuts import render
import numpy as np
import django_filters
from rest_framework import generics, serializers, filters
from rest_framework.response import Response

from api.models import Respondent, Activity, Demographic


class RespondentSerializer(serializers.ModelSerializer):
    activities = serializers.SerializerMethodField()

    def get_activities(self, obj):
        print("your mom goes to college")
        active = {}
        activities = Activity.objects.filter(respondent=obj)
        for activity in activities:
            if activity.minutes > 0:
                active[str(activity.cat_1 + activity.cat_2 + activity.cat_3)] = activity.minutes
        return active

    class Meta:
        model = Respondent
        fields = ['case_id', 'age', 'sex', 'weight', 'hours_worked_per_week', 'activities']


class DemographicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demographic


class ActivitySerializer(serializers.ModelSerializer):
    filter = serializers.SerializerMethodField()

    def get_filter(self, obj):
        respondent = Respondent.objects.filter()

    class Meta:
        model = Activity


class RespondentListView(generics.ListAPIView):
    queryset = Respondent.objects.all()
    serializer_class = RespondentSerializer
    filter_backend = (filters.DjangoFilterBackend,)
    filter_fields = {'age':['exact', 'lte', 'lt', 'gt']}


class RespondentDetailView(generics.RetrieveAPIView):  # This needs to have an Activity Dictionary added to it.
    queryset = Respondent.objects.all()
    serializer_class = RespondentSerializer


class ActivityDetailView(generics.GenericAPIView):
    # queryset = get_queryset()
    serializer_class = ActivitySerializer
    filter_backend = (filters.DjangoFilterBackend,)
    filter_fields = ["average_minutes"]


    def get_queryset(self):
        print("hey")
        act_code = self.kwargs['pk']
        print(act_code)
        act_code_len = len(act_code)
        if act_code_len == 2:
            return Activity.objects.filter(cat_1=act_code)
        elif act_code_len == 4:
            return Activity.objects.filter(cat_1=act_code[:2], cat_2=act_code[2:4])
        elif act_code_len == 6:
            return Activity.objects.filter(cat_1=act_code[:2], cat_2=act_code[2:4], cat_3=act_code[4:])
        else:
            raise Exception("We don't have that")

    def get_object(self, pk):
        print("Heyllo")
        queryset = self.get_queryset()
        act_obj = {}
        minutes = []
        for activity in queryset:
            minutes.append(activity.minutes)
        act_obj['code'] = pk
        if len(pk) == 2:
            act_obj['codes'] = [pk]
        elif len(pk) == 4:
            act_obj['codes'] = [pk[:2], pk[2:]]
        elif len(pk) == 6:
            act_obj['codes'] = [pk[:2], pk[2:4], pk[4:]]

        act_obj["average_minutes"] = np.mean(minutes)
        act_obj["total_number_of_respondents"] = len(queryset)

        # return JsonResponse(act_obj)  # Imported from django.http ---> will not return a Rest Framework API View
        return Response(act_obj)  # Imported from rest_framework

    def get(self, request, pk, format=None):
        return self.get_object(pk)



class ActivitiesRes():
    pass