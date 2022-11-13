from django import forms
from app.models import Appointment
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm


# SignUp
class CreateAccountForm(UserCreationForm):
    first_name = forms.CharField(max_length=200, required=True)
    last_name = forms.CharField(max_length=200, required=False, help_text='Optional')
    email = forms.EmailField(max_length=200, help_text='Please inform a valid email address')
    address = forms.CharField(max_length=200, required=True, help_text='Please inform a email address')
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'address', 'password1', 'password2')

# Profile update
class AccountDetailsUpdateForm(UserChangeForm):
    first_name = forms.CharField(max_length=50, required=False, help_text='Optional', label='Primeiro Nome')
    last_name = forms.CharField(max_length=50, required=False, help_text='Optional', label='Último Nome')
    email = forms.EmailField(max_length=200, help_text='Required. Please inform a valid email address', label='Endereço de Email')
    address = forms.CharField(max_length=200, required=False, help_text='Optional', label='Morada')
    username = forms.CharField(max_length=25, label='Username')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'address')

# Password update
class AccountPasswordUpdateForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=30, label='Password Atual')
    new_password1 = forms.CharField(max_length=30, label='Nova Password')
    new_password2 = forms.CharField(max_length=30, label='Confirmação da Nova Password')

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


# Schedule appointement
class DateInput(forms.DateInput):
    input_type = 'date'

class NewAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('department', 'date', 'message')    
        widgets = {
            'date': DateInput()
        }

# Check scheduled appointments
class CheckAppointmentsForm(forms.Form):
    
    pass
