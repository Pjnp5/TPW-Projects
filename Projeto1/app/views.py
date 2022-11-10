from django.shortcuts import render
from datetime import datetime

from app.forms import *

def home(request):
    tparams = {
        'title': 'Home Page',
        'year': datetime.now().year,
        'app_name': "App do PP",
    }
    return render(request, 'index.html', tparams)


def contact(request):
    tparams = {
        'title': 'Contact',
        'message': 'Your contact page.',
        'year': datetime.now().year,
    }
    return render(request, 'contact.html', tparams)


def about(request):
    tparams = {
        'title': 'About',
        'message': 'Your application description page.',
        'year': datetime.now().year,
    }
    return render(request, 'about.html', tparams)

def appointment(request):
    data = {}
    if request.method == 'POST':
        print(request.POST)
        form = NewAppointmentForm(request.POST)
        for i in form:
            print(i)
        # print(form.cleaned_data['name'])
        data["form"] = form
        print(data)
    return render(request, 'appointment.html', data)

def login(request):
    tparams = {
        'title': 'Login',
        'message': 'Your application description page.',
        'year': datetime.now().year,
    }
    return render(request, 'login.html', tparams)
