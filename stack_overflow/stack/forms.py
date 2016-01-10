from __future__ import unicode_literals
from .models import Profile, Answers, Tag, Question
from django import forms



class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['email']

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answers
        fields = ['text']

class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ['tag']

class AskQuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['title', 'text']

    def form_valid(self, form):
        current_user = Profile.objects.get(pk=self.request.user.id)
        x = current_user
        x.score += 5
        x.save()
        form.instance.user = current_user
        return super(AskQuestion, self).form_valid(form)




















# class ProfileEditForm(forms.ModelForm):

   # class Meta:
       # model = Profile

        # fields = ['customer', 'staff', 'owner']