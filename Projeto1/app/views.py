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
            department=form.cleaned_data["department"]
            date=form.cleaned_data["date"]
            message=form.cleaned_data["message"]
  
            user_data = User.objects.get(username=request.user.username)
            patient = Patient.objects.get(user=user_data)
            
            appointment = Appointment(patient=patient, department=department, date=date, message=message)
            appointment.save()
            appointment.refresh_from_db()
            return redirect('appointments')
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


def appointmentsView(request): 
    if request.user.is_authenticated:
        data = {}
        if request.method == 'GET':
            data['patients'] = list(Patient.objects.all())
            data['appointments'] = list(Appointment.objects.all())
            
            if not request.user.is_superuser:
                patient = Patient.objects.get(user=User.objects.get(username=request.user.username))
                user_appointments = []
                for ap in data['appointments']:
                    if (patient) == ap.patient:
                        user_appointments.append(ap)
                data['appointments'] = user_appointments
        data["form"] = searchForm()
        return render(request, 'appointments.html', data)

def updateAppointments(request):
    if request.method == 'POST': 
        pass
    else:
        form = UpdateAppointmentForm()
    return render(request, 'updateAppointments.html', {'form': form})

def removeAppointments(request):
    data = {}
    if request.method == 'POST':
        print(request.user.appointments)
    return render(request, 'appointments.html', data)
        #Appointment.objects.get(pk=1).delete()

def departmentsView(request):
    return appointmentsView(request)

def appointmentsSearchView(request):
    data = {}
     # if POST request, process form data
    if request.method == 'POST':
        # create form instance and pass data to it
        form = searchForm(request.POST)
        print(form)
        if form.is_valid():  # is it valid?
            query = form.cleaned_data['query']
            print("query", query)
            patient_result = Appointment.objects.filter(patient__user__username__icontains=query)
            print(patient_result)
            department_result = Appointment.objects.filter(department__name__icontains=query)
            print(department_result)
            message_result = Appointment.objects.filter(message__icontains=query)
            print(message_result)
            results = list(set(list(list(patient_result) + list(department_result) + list(message_result))))
            data['appointments'] = results
            form = searchForm()
            data['form'] = form
            return render(request, 'appointments.html', data)
    # if GET (or any other method), create blank form
    else:
        form = searchForm()
        data['form'] = form
    return render(request, 'index.html', data)

def pageNotFoundView(request):
    out = render(request, 'pagenotfound.html')
    out.status_code = 404
    return out