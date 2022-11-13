from django.shortcuts import render, redirect
from datetime import datetime

from app.forms import *
from app.models import *

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
    if not (request.user.is_authenticated or request.user.username):
        return redirect('login')
    if request.method == 'POST':
        form = NewAppointmentForm(request.POST)
        if form.is_valid():
            print("pylance")
            department=form.cleaned_data["department"]
            date=form.cleaned_data["date"]
            message=form.cleaned_data["message"]
            patient = Patient(user=request.user.username,email=request.user.email,address=request.user.address)
            appointment = Appointment(patient=patient, department=department, date=date, message=message)
            appointment.save()
            appointment.refresh_from_db()
    else:
        form = NewAppointmentForm()
    return render(request, 'appointment.html', {'form': form})


# SignUp
def signup(request):
    if request.method == 'POST': 
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            print("NEW USER INSERTED")
            new_user = form.save()
            email=form.cleaned_data["email"]
            address=form.cleaned_data["address"]
            patient = Patient(user=new_user,email=email,address=address)
            patient.save()
            new_user.refresh_from_db()
            return redirect('login')
    else:
        form = CreateAccountForm()
    return render(request, 'signup.html', {'form': form})


def AppointmentsView(request): 
    if request.user.is_authenticated:
        data = {}
        if request.user.is_superuser:
            if request.method == 'GET':
                patients = []
                for p in Patient.objects.all():
                    patients.append(p)
                data['patients'] = patients
                data['appointments'] = list(Appointment.objects.all())
                print(data)
        else:
            # tem de se mudar
            if request.method == 'GET':
                patients = []
                for p in Patient.objects.all():
                    patients.append(p)
                data['patients'] = patients
                data['appointments'] = list(Appointment.objects.all())
                print(data)
        
        return render(request, 'appointments.html', data)
    