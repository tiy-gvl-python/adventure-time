"""autus_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from api import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^respondents/$', views.RespondentListView. as_view(), name='respondent_list'),
    url(r'^respondent/(?P<pk>\d+)/$', views.RespondentDetailView.as_view(), name='respondent_detail'),
    url(r'^activity/(?P<pk>\d+)/$', views.ActivityDetailView.as_view(), name='activity_detail'),
    url(r'^activities/(?P<pk>\d+)/$', views.ActivitiesRes.as_view(), name='activities_res'),
    url(r'^$', TemplateView.as_view(template_name='docs.html'), name="docs")

]

# (?P<num>\d+)