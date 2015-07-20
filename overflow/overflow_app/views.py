from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.core.urlresolvers import reverse_lazy, reverse
from .models import Question, UserProfile, Reply


# Create your views here.


# Thread/Topic section

'''
class ThreadCreateView(CreateView):
    model = ConversationThread
    success_url = reverse_lazy('NEEDSTOGETOUT:thread_list')
    fields = ['user', 'timestamp']
'''
'''
    def form_valid(self, form):
        form.instance.user = UserProfile.objects.get(user=self.request.user)
        return super().form_valid(form)
'''

class QuestionListView(ListView):
    model = Question
    success_url = reverse_lazy('question_list')
    template = "templates/question_list.html"

'''
class ThreadDeleteView(DeleteView):
    model = ConversationThread
    success_url = reverse_lazy('NEEDSTOGETOUT:Moderator_thread_list')


class ThreadUpdateView(UpdateView):
    model = ConversationThread
    success_url = reverse_lazy('NEEDSTOGETOUT:admin_comment_list')
    fields = ['user', 'update', 'recommend']


class ModeratorThreadListView(ListView):
    model = Comment
    success_url = reverse_lazy('restaurant_app:admin_comment_list')
    template = "admin_comment_list.html"


# end Thread/Topic section

# Post/Reply section

class PostCreateView(CreateView): #comment customer view
    model = PostReply
    success_url = reverse_lazy('NEEDSTOGETOUT:comment_list')
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
    '''