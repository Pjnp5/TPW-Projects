from django import forms
from app.models import Appointment
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm


class NewAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('name', 'email')
        # fields = ("id", "user", "doctor", "dept", "date", "form_message")