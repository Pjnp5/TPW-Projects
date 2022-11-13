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

class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.name)

class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date = models.DateField()
    message = models.CharField(max_length=200)

    def __str__(self):
        return str(f"{self.patient} {self.department} {self.date}")


