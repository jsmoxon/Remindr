from django.db import models
import datetime
from django.contrib.auth.models import User, Permission, Group

class Reminder(models.Model):
    person = models.ForeignKey(User)
    title = models.CharField(max_length=1000)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(null=True, blank=True)
    date_to_remind = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)
    def __unicode__(self):
        return self.title
