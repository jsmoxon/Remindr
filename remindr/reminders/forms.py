from django.forms.models import ModelForm
from django.forms.fields import DateField
from django.forms.extras.widgets import SelectDateWidget
from models import Reminder

class AddReminderForm(ModelForm):
    class Meta:
        model = Reminder
        fields = ('title', 'description', 'date_to_remind')

