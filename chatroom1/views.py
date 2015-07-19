from django.views import
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.edit import FormView
from django.template import RequestContext
from django.utils.decorators import method_decorator
from .models import PostReply, UserProfile, ConversationThread
from .forms import ProfileForm, ProfileEditForm

# Create your views here.


# Thread/Topic section

class ThreadCreateView(CreateView):
    model = ConversationThread
    success_url = reverse_lazy('chatroom1:thread_list')
    fields = ['user', 'timestamp']
'''
    def form_valid(self, form):
        form.instance.user = UserProfile.objects.get(user=self.request.user)
        return super().form_valid(form)
'''

class ThreadDeleteView(DeleteView):
    model = ConversationThread
    success_url = reverse_lazy('chatroom1:moderator_thread_list')


class ThreadUpdateView(UpdateView):
    model = ConversationThread
    success_url = reverse_lazy('restaurant_app:admin_comment_list')
    fields = ['user', 'timestamp', 'recommend']


class AdminCommentListView(ListView):
    model = Comment
    success_url = reverse_lazy('restaurant_app:admin_comment_list')
    template = "admin_comment_list.html"


class CommentListView(ListView):
    model = Comment
    success_url = reverse_lazy('restaurant_app:comment_list')
    template = "comment_list.html"

# end Thread/Topic section

# Post/Reply section

class PostCreateView(CreateView): #comment customer view
    model = PostReply
    success_url = reverse_lazy('chatroom1:comment_list')
    fields = ['user', 'timestamp']

    def form_valid(self, form):
        form.instance.user = UserProfile.objects.get(user=self.request.user)
        return super().form_valid(form)


class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy('restaurant_app:admin_comment_list')


class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['user', 'comment', 'recommend']
    success_url = reverse_lazy('restaurant_app:admin_comment_list')

class AdminCommentListView(ListView):
    model = Comment
    success_url = reverse_lazy('restaurant_app:admin_comment_list')
    template = "admin_comment_list.html"


class CommentListView(ListView):
    model = Comment
    success_url = reverse_lazy('restaurant_app:comment_list')
    template = "comment_list.html"