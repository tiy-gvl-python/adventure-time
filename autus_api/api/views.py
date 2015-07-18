from django.shortcuts import render
from rest_framework import generics, serializers

from api.models import Respondent, Activity, Demographic


class RespondentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Respondent


class DemographicSerializer(serializers.ModelSerializer):


    class Meta:
        model = Demographic


class ActivitySerializer(serializers.ModelSerializer):


    class Meta:
        model = Activity


class RespondentListView(generics.ListAPIView):
    queryset = Respondent.objects.all()
    serializer_class = RespondentSerializer


class RespondentDetailView(generics.RetrieveAPIView): #  This needs to have an Activity Dictionary added to it.
    queryset = Respondent.objects.all()
    serializer_class = RespondentSerializer
