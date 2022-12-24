"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from drf_api import views

# from drf_api.views import LoginView, LogoutView, UserView

urlpatterns = [
    path('admin/', admin.site.urls),

    # developed web services
    path('ws/appointments', views.getAllAppointments),
    # path('ws/appointment', views.getAppointment),
    # path('ws/appointment/create', views.createAppointment),
    # path('ws/appointment/update', views.updateAppointment),
    # path('ws/appointment/delete/<int:id>', views.deleteAppointment),

    # path('ws/departments', views.getAllDepartments),
    # path('ws/department', views.getDepartment),
    # path('ws/department/create', views.createDepartment),
    # path('ws/department/update', views.updateDepartment),
    # path('ws/department/delete/<int:id>', views.deleteDepartment),

    # path('ws/signup', views.signup),
    # path('ws/login', views.login),
    # path('ws/logout', views.logout),
    # path('ws/user', views),
]
