from django import forms
from django.forms import ModelForm

from orion.models import Event


class EventForm(ModelForm):

    class Meta:
        model = Event
        exclude = [' date_creation', 'user', 'subdivision']
