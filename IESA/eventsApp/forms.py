# eventsApp/forms.py
from datetime import date

from django import forms
from .models import Event, Participant

class EventsRegistrationForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'date_of_birth']

        def clean_date_of_birth(self):
            date_of_birth = self.cleaned_data['date_of_birth']
            today = date.today()

            if date_of_birth and date_of_birth > today:
                raise forms.ValidationError("Date of birth cannot be in the future.")

            return date_of_birth