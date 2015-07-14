__author__ = 'oqqrez'

from django.forms import ModelForm
from studedit.models import Groups

class GroupForm(ModelForm):
    class Meta:
        model = Groups
        fields = ['name', 'faculty']