from rest_framework import serializers
from WalkinClinicApp.models import Patients, Staff, Appointments, Prescription

class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = ('Id','Name','Address','Phone','pin' )

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('Id','Name','Address','Phone','pin','RoleId')
        
class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = ('Id','PatientId','PatientName','Address','Phone','pin','Email','Gender','AppointmentTypeId','AppointmentDate','AppointmentTime')
                  
class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ('Id','PatientName','PatientId','DocterName','DocterId','Date','MedicineId')
                  
