from django.shortcuts import render_to_response
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from models import *
from django.core.mail import send_mail, BadHeaderError
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
import string, datetime
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from forms import *

@login_required
def home(request):
    def get_queryset(self):
        return self.request.user.book_set.filter(active=True)
    return render_to_response("entry.html")

@login_required
def stored_successfully(request):
    return HttpResponse("Stored successfully!")

class AddReminderView(CreateView):
    model = Reminder
    form_class = AddReminderForm
    template_name = "add_reminder.html"
    success_url = "success"
    def get_form(self, form_class):
        form = super(AddReminderView, self).get_form(form_class)
        form.instance.person = self.request.user
        return form
    


@csrf_exempt
def create_reminder(request):
    reminder = Reminder.objects.create(title=request.POST['title'])
    today = datetime.datetime.today()
    now = datetime.datetime.now()
    reminder.date_created = now
    reminder.save()
    reminder.description = request.POST['description']
    reminder.date_to_remind = request.POST['date_to_remind']
    reminder.save()
    subject = reminder.title
    message = "You have created a reminder called %s. You will be reminded of it later." % reminder.title
    from_email = "remindr.email@gmail.com"
    TO = "jsmoxon@gmail.com"
    body = string.join((
            "From: %s" % from_email,
            "Subject: %s" % subject,
            "To: %s" % TO,
            message,
            ), "\r\n")
    send_mail(subject, body, from_email, ['jsmoxon@gmail.com'], fail_silently=False)
    return HttpResponse("Sent!")

def send_reminder(request):
    now = datetime.datetime.now()
    reminder_list = Reminder.objects.all()
    for reminder in reminder_list:
        if reminder.date_to_remind < now:
            subject = reminder.title
            message = str(reminder.date_to_remind)
            from_email = "remindr.email@gmail.com"
            TO = "jsmoxon@gmail.com"
            body = string.join((
                    "From: %s" % from_email,
                    "Subject: %s" % subject,
                    "To: %s" % TO,
                    message,
                    ), "\r\n")
            send_mail(subject, body, from_email, ['jsmoxon@gmail.com'], fail_silently=False)   
        else:
            subject = reminder.title
            message = reminder.description+"and here is a bit of text to mix it up"
            from_email = "remindr.email@gmail.com"

            send_mail(subject, "Has not occurred yet", "remindr.email@gmail.com", ['jsmoxon@gmail.com'], fail_silently=False)
    return HttpResponse("Thanks!")

def cron_reminder():
    now = datetime.datetime.now()
    reminder_list = Reminder.objects.all()
    for reminder in reminder_list:
        if reminder.date_to_remind < now:
            subject = reminder.title
            message = str(reminder.date_to_remind)
            from_email = "remindr.email@gmail.com"
            TO = "jsmoxon@gmail.com"
            body = string.join((
                    "From: %s" % from_email,
                    "Subject: %s" % subject,
                    "To: %s" % TO,
                    message,
                    ), "\r\n")
            send_mail(subject, body, from_email, ['jsmoxon@gmail.com'], fail_silently=False)
        else:
            subject = reminder.title
            message = reminder.description+"and here is a bit of text to mix it up"
            from_email = "remindr.email@gmail.com"
            send_mail(subject, "Has not occurred yet", "remindr.email@gmail.com", ['jsmoxon@gmail.com'], fail_silently=False)


def reminder_confirmation(reminder):
    reminder = Reminder.objects.get(pk=1)
    subject = reminder.title
    message = reminder.description
    from_email = "remindr.email@gmail.com"
    TO = "jsmoxon@gmail.com"
    body = string.join((
            "From: %s" % from_email,
            "Subject: %s" % subject,
            "To: %s" % TO,
            message,
            ), "\r\n")
    send_mail(subject, body, from_email, ['jsmoxon@gmail.com'], fail_silently=False)
    return HttpResponse("Sent!")

def cron_test():
    send_mail("this is a test of the cron system", "this is only a test", "remindr.email@gmail.com", ['jsmoxon@gmail.com'], fail_silently=False)

class ReminderView(ListView):
    context_object_name = "reminder_list"
    template_name = "reminders.html"
    model = Reminder
    def get_queryset(self):
        return self.request.user.reminder_set.filter(active=True)
