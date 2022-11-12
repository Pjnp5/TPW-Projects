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



# SignUp
def signup(request):
    if request.method == 'POST': 
        print("POST: ", request.POST)   
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            print("NEW USER INSERTED")
            new_user = form.save()
            patient = Patient(user=new_user)
            patient.save()
            new_user.refresh_from_db()
            return redirect('index')
        else:
            print("pylance 2222")
    else:
        form = CreateAccountForm()
    return render(request, 'signup.html', {'form': form})


# Logout user
# def account_logout(request):
#     Order.objects.filter(id=request.session['session']).delete()
#     logout(request)
#     return redirect('login')
