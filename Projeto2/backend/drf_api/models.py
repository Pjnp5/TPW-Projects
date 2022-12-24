from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_dean = models.BooleanField(default=False)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(f"Patient [ID: {self.id}, Name: {self.user.first_name} {self.user.last_name}]")

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(f"Doctor [ID: {self.id}, Name: {self.user.first_name} {self.user.last_name}]")

class Dean(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(f"Dean [ID: {self.id}, Name: {self.user.first_name} {self.user.last_name}]")

class Department(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    doctors = models.ManyToManyField(Doctor)

    def __str__(self):
        return str(f"Department [ID: {self.id}, Name: {self.name}]")

class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    date = models.DateField()
    message = models.CharField(max_length=200)

    def __str__(self):
        return str(f"Appointment [ID: {self.id}, Patient: {self.patient}, Department: {self.department}, Date: {self.date}]")

class Prescription(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    message = models.CharField(max_length=200)

    def __str__(self):
        return str(f"Prescription [ID: {self.id}, Patient: {self.patient}, Doctor: {self.doctor}, Date: {self.date}]")