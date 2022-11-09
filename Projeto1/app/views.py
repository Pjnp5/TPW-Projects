from django.shortcuts import render
from datetime import datetime

# GET

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
    tparams = {
        'title': 'Appointment',
        'message': 'Your application description page.',
        'year': datetime.now().year,
    }
    return render(request, 'appointment.html', tparams)

def login(request):
    tparams = {
        'title': 'Login',
        'message': 'Your application description page.',
        'year': datetime.now().year,
    }
    return render(request, 'login.html', tparams)
