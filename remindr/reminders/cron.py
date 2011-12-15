from django_cron import cronScheduler, Job
from reminders.views import send_reminder
from models import Reminder
from datetime import datetime
from django.contrib.auth.models import User

class sendMail(Job):
    run_every = 100

    def job(self):
        cron_test()

cronScheduler.register(sendMail)

