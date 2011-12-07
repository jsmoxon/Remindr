from django.conf.urls.defaults import patterns, include, url
from views import ReminderView, AddReminderView, MainView
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from models import *

urlpatterns = patterns('',
#    url(r'^home', login_required(MainView.as_view(), login_url='/'), name='main'),
    url(r'^home', login_required(ReminderView.as_view(), login_url='/'), name='home'),
    url(r'^add', login_required(AddReminderView.as_view(), login_url='/'), name='add'),
    url(r'^success', 'reminders.views.stored_successfully', name='stored_successfully'),
)
