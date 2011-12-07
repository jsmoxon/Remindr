from models import *

def counter():
    reminder_list = Reminders.objects.all()
    for reminder in reminder_list:
        reminder.description += "test"
        reminder.save()
        return
