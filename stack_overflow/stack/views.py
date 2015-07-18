from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from .forms import ProfileForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView
from .models import Profile, Question, Tag, Count, Vote, Answers
from django.core.urlresolvers import reverse_lazy, reverse

# Create your views here.


def home(request):
    # needs to show top questions
    return HttpResponse('This is the Homepage space')


def user_registration(request):
    if request.POST:
        ok = True
        user_creation_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if not user_creation_form.is_valid():
            ok = False
        if not profile_form.is_valid():
            ok = False
        if ok:
            print('it should work')
            try:
                users = user_creation_form.save()
                profile = profile_form.save(commit=False)
                profile.user = users
                profile.save()
                return redirect('stack:Login')
            except:
                return render_to_response("registration/create_user.html",
                                      {'u_form': UserCreationForm, 'p_form': ProfileForm},
                                      context_instance=RequestContext(request))
    return render_to_response("registration/create_user.html",
                                  {'u_form': UserCreationForm, 'p_form': ProfileForm},
                                  context_instance=RequestContext(request))


def permission_denied(requests):
    return render_to_response("stack/permission_denied.html",
                              context_instance=RequestContext(requests))

class ListOfUsers(ListView):
    model = Profile

def user_profile(request, user_id):
    try:
        profile = Profile.objects.get(pk=user_id)
    except Profile.DoesNotExist:
        return HttpResponseNotFound('<h1>No Page Here</h1>')
    if Question.objects.filter(pk=user_id):
        questions = Question.objects.filter(pk=user_id)
        context = {"profile": profile, 'user': profile.user, 'questions': questions}
    else:
        context = {"profile": profile, 'user': profile.user}
    return render_to_response("stack/user-profile.html",
                              context, context_instance=RequestContext(request))


class ListOfQuestions(ListView):
    model = Question

class QuestionPage(DetailView):
    model = Question
    
    def get_context_data(self, **kwargs):
        context = super(QuestionPage, self).get_context_data()
        context['answers'] = Answers.objects.filter(question=2)
        return context

class AskQuestion(CreateView):
    model = Question

