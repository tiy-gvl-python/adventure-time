from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.views.generic import ListView, DetailView, CreateView
from .models import Question, Answer, Tag


# Create your views here.

class QuestionCreateView(CreateView):
    model = Question
    fields = ['title', 'question']
    success_url = reverse_lazy('question_list')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AnswerCreateView(CreateView):
    model = Answer
    fields = ['question', 'answer']
    success_url = reverse_lazy('question_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'question_detail.html'


class QuestionListView(ListView):
    model = Question
    template_name = 'question_list.html'


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
