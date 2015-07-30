__author__ = 'oqqrez'

from django.forms import ModelForm
from studedit.models import Students


class StudentForm(ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'family', 'group']

