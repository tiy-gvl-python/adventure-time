from django.contrib import admin
from overflow_app.models import Question, UserProfile, Reply

# Register your models here.

admin.site.register(Question)
admin.site.register(UserProfile)
admin.site.register(Reply)