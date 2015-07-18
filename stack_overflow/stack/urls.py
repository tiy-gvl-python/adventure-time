from django.conf.urls import include, url
from django.contrib.auth.views import login, logout
from django.views.generic import CreateView
from .views import user_registration, home, ListOfUsers, user_profile, ListOfQuestions, permission_denied, \
    QuestionPage


SLUG = '(?P<slug>[\w\d-]+)'

urlpatterns = [

    url(r'^$', home, name='home'),
    url(r'register/$', user_registration, name='register'),
    url(r'^login/', login, name='Login'),
    url(r'^logout/', logout, {'next_page': '/'}, name='Logout'),
    url(r'^users/$', ListOfUsers.as_view(), name='ListOfUsers'),
    url(r'^users/(?P<user_id>\d+)/$', user_profile, name='Profile'),
    url(r'questions/$', ListOfQuestions.as_view(), name='QuestionList'),
    url(r'questions/(?P<pk>\d+)/$', QuestionPage.as_view(), name='question_page'),
    url(r'denied', permission_denied, name='denied'),

]
