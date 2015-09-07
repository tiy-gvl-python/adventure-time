from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.generic import ListView, DetailView, CreateView
from .models import Question, Answer, UserProfile
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import serializers


# Create your views here.


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        field = 'question'


class QuestionListAPIView(ListCreateAPIView):
    model = Question
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetailAPIView(RetrieveUpdateDestroyAPIView):
    model = Question
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionCreateView(CreateView):
    model = Question
    fields = ['title', 'question']
    success_url = reverse_lazy('question_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        up = UserProfile.objects.get(user=self.request.user)
        up.reputation += 5
        up.save()
        return super().form_valid(form)


class AnswerCreateView(CreateView):
    model = Answer
    fields = ['answer']
    success_url = reverse_lazy('question_list')

    def form_valid(self, form):
        print(self.kwargs)
        question_pk = self.kwargs['pk']
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


def upvote(request):
    if request.method == 'POST':
        answerobject = Answer.objects.get(id=request.POST['next'])
        answerobject.reputation += 1
        answerobject.save()
        # -
        answeruserprofile = UserProfile.objects.get(user=answerobject.user)
        answeruserprofile.reputation += 10
        answeruserprofile.save()
        return redirect(reverse_lazy('question_detail', kwargs={'pk': answerobject.question.id}))


def downvote(request):
    if request.method == 'POST':
        answerobject = Answer.objects.get(id=request.POST['next'])
        answerobject.reputation -= 1
        answerobject.save()
        down = UserProfile.objects.get(user=request.user)
        down.reputation -= 1
        down.save()
        answeruserprofile = UserProfile.objects.get(user=answerobject.user)
        answeruserprofile.reputation -= 5
        answeruserprofile.save()
        print(reverse_lazy('question_detail', kwargs={'pk': answerobject.question.id}))
        return redirect(reverse_lazy('question_detail', kwargs={'pk': answerobject.question.id}))


def user_detail(request):
    if request.user:
        question = request.user.question_set.all()
        uquestions = {'questions': question}
    return render_to_response('user_detail.html', context=uquestions, context_instance=RequestContext(request))

def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request))
