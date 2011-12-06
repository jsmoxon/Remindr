from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()
import django_cron
django_cron.autodiscover()



urlpatterns = patterns('',
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^$', 'reminders.views.home'),
     url(r'^create_reminder', 'reminders.views.create_reminder'),
     url(r'^reminder_confirmation', 'reminders.views.reminder_confirmation'),
     url(r'^send_reminder', 'reminders.views.send_reminder'),
     url(r'^profiles/', include('profiles.urls')),
     url(r'^reminders/', include('reminders.urls')),
)
