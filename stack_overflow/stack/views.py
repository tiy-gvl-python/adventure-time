import random

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from .forms import ProfileForm, AnswerForm, TagForm, AskQuestionForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView
from .models import Profile, Question, Tag, Count, Vote, Answers
from django.core.urlresolvers import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from .custom_wrappers import can_answer_func, can_ask_func

# Create your views here.


def home(request):
    top_questions = Question.objects.all()[:50]
    return render(request, 'stack/home.html', {'top_questions': top_questions})


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
                try:
                    username = request.POST['username']
                    password = request.POST['password1']
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    return redirect('stack:home')
                except:
                    return redirect('stack:Login')
            except:
                return render_to_response("registration/create_user.html",
                                      {'u_form': UserCreationForm, 'p_form': ProfileForm},
                                      context_instance=RequestContext(request))
    return render_to_response("registration/create_user.html",
                                  {'u_form': UserCreationForm, 'p_form': ProfileForm},
                                  context_instance=RequestContext(request))


def permission_denied(requests):
    return render_to_response("stack/answer_denied.html",
                              context_instance=RequestContext(requests))


def q_denied(requests):
    return render_to_response("stack/question_denied.html",
                              context_instance=RequestContext(requests))


class ListOfUsers(ListView):
    model = Profile

def user_profile(request, user_id):
    current_user = Profile.objects.get(pk=user_id)
    try:
        profile = Profile.objects.get(pk=user_id)
    except Profile.DoesNotExist:
        return HttpResponseNotFound('<h1>No Page Here</h1>')
    if Question.objects.filter(user=current_user):
        questions = Question.objects.filter(user=current_user)
        context = {"profile": profile, 'questions': questions}
    else:
        context = {"profile": profile}
    context['questions'] = Question.objects.filter(user=current_user)
    return render_to_response("stack/user-profile.html",
                              context, context_instance=RequestContext(request))


class ListOfQuestions(ListView):
    model = Question


def question_page(request, question_id):
    try:
        ques = Question.objects.get(pk=question_id)
        if Answers.objects.filter(question=ques):
            answer = Answers.objects.filter(question=ques)
            context = {'question': ques, 'answer': answer}

        else:
            context = {'question': ques}
    except Question.DoesNotExist:
        return HttpResponse('Not Found!')
    return render_to_response('stack/question_detail.html',
                              context,
                              context_instance=RequestContext(request))

class AskQuestion(CreateView):
    model = Question
    fields = ['title', 'text',  'tags']
    success_url = reverse_lazy('stack:home')

    def form_valid(self, form):
        current_user = Profile.objects.get(pk=self.request.user.id)
        x = current_user
        x.score += 5
        x.save()
        form.instance.user = current_user
        return super(AskQuestion, self).form_valid(form)

    @method_decorator(user_passes_test(can_ask_func,
                                       redirect_field_name='stack:Q_denied',
                                       login_url='stack:Q_denied',
                                       ))
    def dispatch(self, *args, **kwargs):
        print("user passed test", can_ask_func)
        return super().dispatch(*args, **kwargs)


class TagCreation(CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy('stack:AskQuestion')
    success_message = "Tag created succsefully"

    def form_valid(self, form):
        if Tag.objects.filter(tag=self.request.POST['tag']):
            return HttpResponse("TAG ALREADY EXIST")
        else:
            return super(TagCreation, self).form_valid(form)

@login_required(login_url='stack:Login')
@user_passes_test(can_ask_func, login_url='stack:Q_denied')
def ask_question(request):
    context = {}
    ok = True
    print('UNDER TRUE')
    ask_form = AskQuestionForm(request.POST)
    tag_form = TagForm(request.POST)
    context['ask_form'] = ask_form
    context['tag_form'] = tag_form
    print("B")
    if not ask_form.is_valid():
        print("Ba")
        ok = False
    if ok:
        print('Bam')
        if tag_form.is_valid():
            print('Here')
            question = ask_form.save()
            print('1')
            try:
                tag = tag_form.save(commit=False)
                print('2')
                if Tag.objects.all().filter(tag=tag.tag):
                    print('3')
                    tag = Tag.objects.all().get(tag=tag.tag)
                    print('4')
                else:
                    print('5')
                    tag = tag_form.save(commit=True)
                    print('6')
                question.tags.add(tag)
                print('7')
                question.save(commit=True)
                print('8')
                return redirect("question_page", question.pk)
            except:
                print('There')
                try:
                    question = ask_form.save()
                    return redirect("question_page", question.pk)
                except:
                    return render_to_response('stack/answer_question_func.html',
                                                context,
                                                context_instance=RequestContext(request))
        else:
            try:
                question = ask_form.save()
                return redirect("question_page", question.pk)
            except:
                return render_to_response('stack/answer_question_func.html',
                                            context,
                                              context_instance=RequestContext(request))
    return render_to_response('stack/answer_question_func.html',
                                            context,
                                              context_instance=RequestContext(request))


@login_required(login_url='stack:Login')
@user_passes_test(can_answer_func, login_url='stack:A_denied')
def answer_question(request, question_id):
    if request.POST:
        user_id = request.user.id
        question = Question.objects.get(pk=question_id)
        print('Question: {}'.format(question))
        usr = request.user
        ok = True
        answer_form = AnswerForm(request.POST)
        if not answer_form.is_valid():
            ok = False
        if ok:
            print('answer form at second if')
            try:
                print('answer_form at try')
                answer = answer_form.save(commit=False)
                answer.user = usr.profile
                answer.question = question
                answer.save()
                print('answer_form made it to end of try')
                return redirect('stack:question_page', question_id)
            except:
                answer.user = usr.profile
                answer.question = question
                answer.save()
                print('answer_form hit except')
                return render_to_response('stack/answer_question.html',
                                          {'answer_form': AnswerForm},
                                          context_instance=RequestContext(request))
    return render_to_response('stack/answer_question.html',
                                          {'answer_form': AnswerForm},
                                          context_instance=RequestContext(request))


def vote_create(request, votee_pk, model_type, vote_type='upvote'):
    print('here') # separate this out into more than one function so that
    if model_type == 'answer':
        obj = Answers.objects.get(pk=votee_pk)
        x_var = obj.question.pk
    else:
        x_var = votee_pk    # people can only vote on one question at a time
    if request.POST:
        print('sent post')
        user_pk = request.user.pk
        profile = Profile.objects.get(pk=user_pk)
        if not Vote.objects.filter(votee_pk=votee_pk).filter(voter=profile):
            question = False
            answer = False
            downvote = False
            upvote = True
            profile = Profile.objects.get(pk=user_pk)
            model_type = model_type
            obj = ''
            if model_type == 'question':
                question = True
                obj = Question.objects.get(pk=votee_pk)
            if model_type == 'answer':
                obj = Answers.objects.get(pk=votee_pk)
                answer = True
            if vote_type == 'downvote':
                downvote = True
                upvote = False
                owner = Profile.objects.get(pk=obj.user.pk)
                obj.score -= 5
                obj.save()
                if profile.score > 0:
                    profile.score -= 1
                    profile.save()
                if owner.score > 5:
                    owner.score -= 5
                    owner.save()
            else:
                numset = '000000001'
                if profile.score < 25:
                    numset = '010021'
                rand = random.choice(numset)
                owner = Profile.objects.get(pk=obj.user.pk)
                owner.score += 10
                print('It works here is the owners score:', owner.score)
                profile.score += int(rand)
                profile.save()
                obj.score += 10
                obj.save()
                owner.save()
            vote = Vote.objects.create(votee_pk=votee_pk,
                                           voter=profile,
                                           upvote=upvote,
                                           downvote=downvote,
                                           completed=True,
                                           is_question=question,
                                           is_answer=answer)
            vote.save()
        else:
            pass
        return redirect('stack:question_page', question_id=x_var)
    else:
       return redirect('stack:question_page', question_id=x_var)


@login_required(login_url='stack:Login')
def add_25_points(request):
    user_pk = request.user.pk
    profile = Profile.objects.get(pk=user_pk)
    profile.score = profile.score + 25
    profile.save()
    return redirect('stack:home')


@login_required(login_url='stack:Login')
def add_25_points_2(request):
    user_pk = request.user.pk
    profile = Profile.objects.get(pk=user_pk)
    profile.score = profile.score + 25
    profile.save()
    return redirect('stack:AskQuestion')


@login_required(login_url='stack:Login')
def add_125_points(request):
    user_pk = request.user.pk
    profile = Profile.objects.get(pk=user_pk)
    profile.score = profile.score + 125
    profile.save()
    return redirect('stack:home')

