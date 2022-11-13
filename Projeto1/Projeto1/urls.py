"""Projeto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('appointment/', views.appointment, name='appointment'),
    path('appointments/', views.appointmentsView, name='appointments'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', next_page='/'), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('updateAppointments/', views.updateAppointments, name='updateAppointment'),
    path('removeAppointments/', views.removeAppointments, name='removeAppointments'),
    path('signup/', views.signup, name='signup'),
     path('pagenotfound/', views.pageNotFoundView, name='page not found'),


    # ADMIN
    path('appointments/search/', views.appointmentsSearchView, name='appointments'),
    path('appointments/', views.appointmentsView, name='admin/appointments'),
    path('departments/', views.departmentsView, name='admin/departments'),
    path('contacts/', views.home, name='admin/contacts')
]
