# from django.shortcuts import render
from drf_api.models import *
from drf_api.permissions import *
from drf_api.serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# Create your views here.


@api_view(['GET'])
# @permission_classes([IsPatient, IsDoctor, IsDean])
def getAllAppointments(request):
    appoitments = Appointment.objects.all()
    serializer = AppointmentSerializer(appoitments, many=True)
    return Response(serializer.data)
