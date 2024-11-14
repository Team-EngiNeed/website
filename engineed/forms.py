from django import forms
from . import models

class Ticket(forms.ModelForm):
  class Meta:
    model = models.Submission
    fields = ['fullName', 'gradeSection', 'dateSubmitted', 'damagedProperty', 'comment']
    widgets = {
            'dateSubmitted': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }