from __future__ import unicode_literals
from .models import Profile, Answers
from django import forms



class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['email']

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answers
        fields = ['text']







# class ProfileEditForm(forms.ModelForm):

   # class Meta:
       # model = Profile

        # fields = ['customer', 'staff', 'owner']