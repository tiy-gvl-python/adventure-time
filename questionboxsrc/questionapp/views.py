from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response, redirect, get_object_or_404, HttpResponse
from django.template import RequestContext
from django.views.generic import ListView, DetailView, CreateView, FormView
# from django.views.generic.edit import BaseCreateView
from .models import Question, Answer, Tag, UserProfile


# Create your views here.

class QuestionCreateView(CreateView):
    model = Question
    fields = ['title', 'question',]
    success_url = reverse_lazy('question_list')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AnswerCreateView(CreateView):
    model = Answer
    fields = ['answer']
    success_url = reverse_lazy('question_list')

    def form_valid(self, form):
        # print(self.kwargs)
        question_pk = self.kwargs['pk']
        # question_user =
        # print(question_pk)
        # Question.objects.get(id=question_pk)
        form.instance.user = self.request.user
        form.instance.question = Question.objects.get(id=question_pk)
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


def upvote(request):
    if request.method == 'POST':
        answerobject = Answer.objects.get(id=request.POST['next'])
        answerobject.reputation += 1
        answerobject.save()
        # print('answerobject', answerobject.reputation)
        answeruserprofile = UserProfile.objects.get(user=answerobject.user)
        answeruserprofile.reputation += 10
        answeruserprofile.save()
        # print('answeruserprofile', answeruserprofile.reputation)
        return redirect(reverse_lazy('question_detail', kwargs={'pk': answerobject.question.id}))


def downvote(request):
    if request.method == 'POST':
        answerobject = Answer.objects.get(id=request.POST['next'])
        answerobject.reputation -= 1
        answerobject.save()
        # -
        answeruserprofile = UserProfile.objects.get(user=answerobject.user)
        answeruserprofile.reputation -= 5
        answeruserprofile.save()
        # -
        return redirect(reverse_lazy('question_detail', kwargs={'pk': answerobject.question.id}))
