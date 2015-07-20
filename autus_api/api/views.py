from django.http import JsonResponse
from django.shortcuts import render
import numpy as np
import django_filters
from rest_framework import generics, serializers, filters
from rest_framework.response import Response

from api.models import Respondent, Activity, Demographic


class ResActSerializer(serializers.ModelSerializer):
    activities = serializers.SerializerMethodField()
    filt = serializers.SerializerMethodField()

    def restore_fields(self, data, files):
        print("hey")
    def get_filt(self, obj):
        return self._context['request'].QUERY_PARAMS

    def get_activities(self, obj):

        act_id = self._kwargs['context']['view'].kwargs['pk']
        respondent = self._args[0]
        act_obj = {}
        minutes = []
        act_obj['code'] = act_id
        print("actid", act_id)
        if len(act_id) == 2:
            print("Two")
            act_obj['codes'] = [act_id]
            act_list = Activity.objects.filter(respondent__in=respondent, cat_1=act_id)
            print(act_list)
        elif len(act_id) == 4:
            print("Four")
            act_obj['codes'] = [act_id[:2], act_id[2:]]
            act_list = Activity.objects.filter(respondent__in=respondent, cat_1=act_id[:2], cat_2=act_id[2:])
            print(act_list)
        elif len(act_id) == 6:
            print("six")
            act_obj['codes'] = [act_id[:2], act_id[2:4], act_id[4:]]
            act_list = Activity.objects.filter(respondent__in=respondent , cat_1=act_id[:2], cat_2=act_id[2:4], cat_3=act_id[4:])
            print(act_list)
        for act in act_list:
            minutes.append(act.minutes)
        act_obj["average_minutes"] = np.mean(minutes)
        act_obj["total_number_of_respondents"] = len(respondent)
        print("Length o", len(act_obj))
        print("activity", act_obj)
        return act_obj

    class Meta:
        model = Respondent
        fields = ['activities', 'filt']


class RespondentSerializer(serializers.ModelSerializer):
    activities = serializers.SerializerMethodField()

    def get_activities(self, obj):
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
    print('hello')
    def get_filter(self, obj):
        respond = {}
        respondent = Respondent.objects.filter()
        return respond

    class Meta:
        model = Activity


class RespondentListView(generics.ListAPIView):
    # queryset = Respondent.objects.all()
    serializer_class = RespondentSerializer
    filter_backend = (filters.DjangoFilterBackend,)
    filter_fields = {'age':['exact', 'lte', 'lt', 'gt']}

    def get_queryset(self):
        print("h")
        slic = int(self.kwargs['num'])
        return Respondent.objects.all()[:slic]



class RespondentDetailView(generics.RetrieveAPIView):
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


class ActivitiesRes(generics.ListAPIView):
    #print("Hey")
    #queryset = Activity.objects.filter()
    serializer_class = ResActSerializer
    filter_backend = (filters.DjangoFilterBackend,)
    filter_fields = {'sex': ['exact','lt', 'gt','lte', 'gte'], 'age': ['exact','lt', 'gt','lte', 'gte'],
                     'hours_worked_per_week': ['exact','lt', 'gt','lte', 'gte' ]}
    def get_queryset(self):
        print("eh")
        act_code = self.kwargs['pk']
        print(act_code)
        act_code_len = len(act_code)
        if act_code_len == 2:
            print("hey")
            act_set = Activity.objects.filter(cat_1=act_code).values_list('respondent')
            print(act_set)
            print("Y")
            list_of_ids = [id[0] for id in act_set]
            return Respondent.objects.filter(pk__in=list_of_ids)
        elif act_code_len == 4:
            print("Ho")
            act_set = Activity.objects.filter(cat_1=act_code[:2], cat_2=act_code[2:4]).values_list('respondent')
            print(act_set)
            print("Y")
            # return [Respondent.objects.get(id=id[0]) for id in act_set]
            list_of_ids = [id[0] for id in act_set]
            return Respondent.objects.filter(pk__in=list_of_ids)
        elif act_code_len == 6:
            print("hey")
            act_set = Activity.objects.filter(cat_1=act_code[:2], cat_2=act_code[2:4], cat_3=act_code[4:]).values_list('respondent')
            print(act_set)
            print("Y")
            # return [Respondent.objects.get(id=id[0]) for id in act_set]
            list_of_ids = [id[0] for id in act_set]
            return Respondent.objects.filter(pk__in=list_of_ids)
            # return Activity.objects.filter(cat_1=act_code[:2], cat_2=act_code[2:4], cat_3=act_code[4:])
        else:
            raise Exception("We don't have that")


    """def list(self, request, *args, **kwargs):
        print("Hey Yo LETS GO")
        print(request.parsers)
        data = request.parsers[0]
        print("Hey")
        #return super()
        return Response(data=request.parsers)"""

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        print(response)
        print(len(response.data))
        response.data = response.data[0]
        print(len(response.data))
        return response
