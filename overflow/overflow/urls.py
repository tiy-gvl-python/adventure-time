"""chatroom URL Configuration

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
from overflow_app.views import QuestionListView, QuestionCreateView, QuestionDeleteView, QuestionUpdateView


urlpatterns = [
    url(r'^question_update/', QuestionUpdateView.as_view(), name='question_update'),
    url(r'^question_delete/', QuestionDeleteView.as_view(), name='question_delete'),
    url(r'^question_form/', QuestionCreateView.as_view(), name='question_form'),
    url(r'^question_create/', QuestionCreateView.as_view(), name='question_create'),
    url(r'^question_list/', QuestionListView.as_view(), name='question_list'),
    url(r'^admin/', include(admin.site.urls)),
]
