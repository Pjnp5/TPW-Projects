from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class Medic(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#     email = models.EmailField()
#     address = models.CharField(max_length=100)
#     credit = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

#     def __str__(self):
#         return self.user.username

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    email = models.EmailField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # doctor: models.CharField(max_length=100) # Doctor, Diagnostic, Psychological 
    # dept: models.CharField(max_length=100) # Departments, Diagnostic, Psychological
    # date: models.DateTimeField(auto_now_add=True)
    # form_message: models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


