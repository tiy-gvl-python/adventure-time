from django.conf.urls import include, url
from django.contrib.auth.views import login, logout
from django.views.generic import CreateView
from .views import user_registration, home, ListOfUsers, user_profile, ListOfQuestions, permission_denied, \
    AskQuestion, question_page, answer_question, TagCreation, vote_create, q_denied, ask_question, add_25_points, \
    add_125_points, add_25_points_2

SLUG = '(?P<slug>[\w\d-]+)'

urlpatterns = [

    url(r'^$', home, name='home'),
    url(r'register/$', user_registration, name='register'),
    url(r'^login/', login, name='Login'),
    url(r'^logout/', logout, {'next_page': 'stack:home'}, name='Logout'),
    url(r'^users/$', ListOfUsers.as_view(), name='ListOfUsers'),
    url(r'^users/(?P<user_id>\d+)/$', user_profile, name='Profile'),
    url(r'^questions/$', ListOfQuestions.as_view(), name='QuestionList'),
    url(r'^questions/(?P<question_id>\d+)/$', question_page, name='question_page'),
    url(r'^denied/$', permission_denied, name='A_denied'),
    url(r'^denied/question/$', q_denied, name='Q_denied'),
    url(r'^ask/$', AskQuestion.as_view(), name='AskQuestion'),
    url(r'^answer/(?P<question_id>\d+)/$', answer_question, name='answer_question'),
    url(r'^tag/$', TagCreation.as_view(), name='TagCreation'),
    url(r'^vote/(?P<votee_pk>\d+)/(?P<model_type>answer|question+)/(?P<vote_type>upvote|downvote+)/$',
        vote_create, name='vote_create'),
    url(r'ask-question/', ask_question, name='ask_question'),
    url(r'add-25/$', add_25_points, name='add_25_points'),
    url(r'add-25-2/$', add_25_points_2, name='add_25_points_2'),
    url(r'add-125/$', add_125_points, name='add_125_points'),

]
