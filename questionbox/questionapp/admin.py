from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import UserProfile, Question, Answer, Tag


admin.site.register(UserProfile)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Tag)
