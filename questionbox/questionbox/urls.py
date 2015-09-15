from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login
from django.views.generic.edit import CreateView
from questionapp.views import QuestionDetailView, AnswerCreateView, QuestionListView, QuestionCreateView, logout_view, \
<<<<<<< HEAD
                              upvote, downvote, user_detail, QuestionListAPIView, QuestionDetailAPIView, home
=======
                              upvote, downvote, user_detail, home
>>>>>>> OnAWS

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout_view, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^question_form/$', QuestionCreateView.as_view(), name='question_form'),
    url(r'^answer_form/$', AnswerCreateView.as_view(), name='answer_form'),
    url(r'^question_detail/(?P<pk>\d+)/$', QuestionDetailView.as_view(), name='question_detail'),
    url(r'^question_detail/(?P<pk>\d+)/answer_form/$', AnswerCreateView.as_view(), name='answer_form'),
    url(r'^question_list/$', QuestionListView.as_view(), name='question_list'),
    url(r'^register/$', CreateView.as_view(template_name='register.html', form_class=UserCreationForm,
                                           success_url='/accounts/login/'), name='register'),
    url(r'^user_detail/$', user_detail, name='user_detail'),
    url(r'^upvote/$', upvote, name='upvote'),
    url(r'^downvote/$', downvote, name='downvote'),

    url(r'^api/questions/$', QuestionListAPIView.as_view(), name='list'),
    url(r'^api/questions/(?P<pk>\d+)$', QuestionDetailAPIView.as_view(), name='retrieve'),
]
