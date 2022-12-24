from drf_api.models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password')

    # def save(self):
    #     user = User(
    #         first_name=self.validated_data['first_name'],
    #         last_name=self.validated_data['last_name'],
    #         email=self.validated_data['email'],
    #         is_patient=self.validated_data['is_patient'],
    #         is_doctor=self.validated_data['is_doctor'],
    #         is_dean=self.validated_data['is_dean']
    #     )
    #     password = self.validated_data['password']
    #     user.set_password(password)
    #     user.save()
    #     return user

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('user',)

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('user',)

class DeanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dean
        fields = ('user',)

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('name', 'doctors')

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('id', 'patient', 'department', 'date')

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ('id', 'patient', 'doctor', 'date')