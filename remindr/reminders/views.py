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
from django.views.generic import TemplateView
from forms import *
from django.contrib.auth import authenticate, login, logout

def cron_test():
    send_mail("this is a test of the cron system", "this is only a test", "remindr.email@gmail.com", ['jsmoxon@gmail.com'], fail_silently=False)

def list(request):
    reminders = Reminder.objects.all()
    return render_to_response('list.html', {"reminders":reminders})

def log_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render_to_response('loggedin.html')
        else:
            return HttpResponse('Please submit a valid password')
    else:
        return HttpResponse('Remindr is in private beta; please check again later.')

def logout_action(request):
    logout(request)
    return render_to_response('logged_out.html')

def test_reminder(user):
    message = user.reminder_set.filter(active=True)
    subject = user.reminder_set.title
    from_email = "remindr.email@gmail.com"
    send_mail(subject, message, from_email, ['jsmoxon@gmail.com'], fail_silently=False)

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

#Views for reminders.urls 
@login_required
def stored_successfully(request):
    return HttpResponse("Stored successfully!")

class MainView(TemplateView):
    template_name = "main.html"
    model = Reminder
    context_object_name = "reminder_list"

class ReminderView(ListView):
    context_object_name = "reminder_list"
    template_name = "reminders.html"
    model = Reminder
    def get_queryset(self):
        return self.request.user.reminder_set.filter(active=True)

class AddReminderView(CreateView):
    model = Reminder
    form_class = AddReminderForm
    template_name = "add_reminder.html"
    success_url = "success"
    def get_form(self, form_class):
        form = super(AddReminderView, self).get_form(form_class)
        form.instance.person = self.request.user
        return form
    def make_date(request):
        year = request.POST.get('year')
        month = request.POST.get('month')
        reminder.date_to_remind = year+"-"+month
        reminder.save()

