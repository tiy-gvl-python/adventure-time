from __future__ import unicode_literals
from .models import Profile
from django import forms



class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['points']


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['customer', 'staff', 'owner']
