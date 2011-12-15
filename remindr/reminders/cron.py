from django_cron import cronScheduler, Job
from django.core.mail import send_mail, BadHeaderError

class sendMail(Job):
    run_every = 120

    def job(self):
        subject = "test of cron system"
        body = "test of cron" 
        from_email = "remindr.email@gmail.com"
        send_mail(subject, body, from_email, ['jsmoxon@gmail.com'], fail_silently=False)

cronScheduler.register(sendMail)
