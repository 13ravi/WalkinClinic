from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from WalkinClinicApp.models import Patients, Staff, Appointments, Prescription
from WalkinClinicApp.serializers import PatientsSerializer, StaffSerializer, AppointmentsSerializer, PrescriptionSerializer
from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def patientsApi(request,id=0):
    if request.method=='GET':
        patients = Patients.objects.all()
        patients_serializer = PatientsSerializer(patients, many=True)
        return JsonResponse(patients_serializer.data, safe=False)

    elif request.method=='POST':
        patients_data=JSONParser().parse(request)
        patients_serializer = PatientsSerializer(data=patients_data)
        if patients_serializer.is_valid():
            patients_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        patients_data = JSONParser().parse(request)
        patients=Patients.objects.get(Id=patients_data['Id'])
        patients_serializer=PatientsSerializer(patients,data=patients_data)
        if patients_serializer.is_valid():
            patients_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        patients=Patients.objects.get(Id=id)
        patients.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

@csrf_exempt
def staffApi(request,id=0):
    if request.method=='GET':
        staff = Staff.objects.all()
        staff_serializer = StaffSerializer(staff, many=True)
        return JsonResponse(staff_serializer.data, safe=False)

    elif request.method=='POST':
        staff_data=JSONParser().parse(request)
        staff_serializer = StaffSerializer(data=staff_data)
        if staff_serializer.is_valid():
            staff_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        staff_data = JSONParser().parse(request)
        staff=Staff.objects.get(Id=staff_data['Id'])
        staff_serializer=StaffSerializer(staff,data=staff_data)
        if staff_serializer.is_valid():
            staff_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        staff=Staff.objects.get(Id=id)
        staff.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


@csrf_exempt
def SaveFile(request):

    file=request.FILES['uploadedFile']
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name,safe=False)


@csrf_exempt
def appointmentsApi(request,id=0):
    if request.method=='GET':
        appointment = Appointments.objects.all()
        appointment_serializer = AppointmentsSerializer( appointment, many=True)
        return JsonResponse(appointment_serializer.data, safe=False)

    elif request.method=='POST':
        appointment_data=JSONParser().parse(request)
        appointment_serializer = AppointmentsSerializer(data=appointment_data)
        if appointment_serializer.is_valid():
            appointment_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        appointment_data = JSONParser().parse(request)
        appointment=Appointments.objects.get(Id=appointment_data['Id'])
        appointment_serializer=AppointmentsSerializer(appointment,data=appointment_data)
        if appointment_serializer.is_valid():
            appointment_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        appointment=Appointments.objects.get(Id=id)
        appointment.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

@csrf_exempt
def prescriptionApi(request,id=0):
    if request.method=='GET':
        prescription = Prescription.objects.all()
        prescription_serializer = PrescriptionSerializer( prescription, many=True)
        return JsonResponse(prescription_serializer.data, safe=False)

    elif request.method=='POST':
        prescription_data=JSONParser().parse(request)
        prescription_serializer = PrescriptionSerializer(data=prescription_data)
        if prescription_serializer.is_valid():
            prescription_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        prescription_data = JSONParser().parse(request)
        prescription=Prescription.objects.get(Id=prescription_data['Id'])
        prescription_serializer=PrescriptionSerializer(prescription,data=prescription_data)
        if prescription_serializer.is_valid():
            prescription_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        prescription=Prescription.objects.get(Id=id)
        prescription.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)



    