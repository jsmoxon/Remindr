from django_cron import cronScheduler, Job
from reminders.views import *

class sendMail(Job):
    run_every = 300

    def job(self):
        cron_reminder()

cronScheduler.register(sendMail)
