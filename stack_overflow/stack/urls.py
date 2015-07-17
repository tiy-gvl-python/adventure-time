from django.conf.urls import include, url
from django.contrib.auth.views import login, logout
from django.views.generic import CreateView
from .views import user_registration, home

urlpatterns = [

    url(r'^$', home, name='home'),
    url(r'register/$', user_registration, name='register'),
    url(r'^login/', login, name='Login'),
    url(r'^logout/', logout, {'next_page': '/'}, name='Logout'),
    url()

]
