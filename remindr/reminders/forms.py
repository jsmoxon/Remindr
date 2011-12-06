from django.forms.models import ModelForm
from models import Reminder

class AddReminderForm(ModelForm):
    class Meta:
        model = Reminder
        fields = ('title', 'date_created', 'description', 'date_to_remind')
