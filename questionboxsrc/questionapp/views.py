import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.core.urlresolvers import reverse_lazy
from django.db import IntegrityError
from django.shortcuts import render, render_to_response, redirect, HttpResponse, get_object_or_404
from django.template import RequestContext
from django.views.generic import ListView, DetailView, CreateView
from .models import Question, Answer, Tag


# Create your views here.

class QuestionForm(CreateView):
    model = Question
    template_name = 'question_form.html'


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'question_detail.html'

    def func(self):
        return

class QuestionListView(ListView):
    model = Question
    template_name = 'question_list.html'

    def get_queryset(self):
        # qs = Question.objects.filter(user=self.request.user)
        return

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request))


def user_questions(request):
    user = get_object_or_404(User, username=User)
    if request.user == user:
        question = user.question.all()
    return render_to_response('user_questions.html', context_instance=RequestContext(request))



'''
        qsid = [trade.id for trade in qs]  # Bekk
        qs = ClosedTrade.objects.filter(pk__in=qsid)  # Bekk
        return qs

         Show all Individual trades for current user regardless of date
        qs = Question.objects.filter(user=self.request.user)
        return qs
'''

'''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("HI Q")
        context['comments'] = Question.objects.filter(trade=self.object)
        return context
'''
