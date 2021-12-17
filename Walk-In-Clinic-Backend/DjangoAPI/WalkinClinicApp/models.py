from django.db import models
import datetime
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Patients(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100) 
    Address= models.CharField(max_length=200)
    Phone= models.CharField(max_length=50)
    pin = models.CharField(max_length=50)

class Staff(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100) 
    Address= models.CharField(max_length=200)
    Phone= models.CharField(max_length=50)
    pin = models.CharField(max_length=50)
    RoleId= models.IntegerField()

class Prescription(models.Model):
    Id = models.AutoField(primary_key=True)
    PatientName = models.CharField(max_length=100)
    PatientId = models.CharField(max_length=100)
    DocterName= models.CharField(max_length=200)
    DocterId = models.CharField(max_length=100)
    Date= models.CharField(max_length=50)
    MedicineId= models.IntegerField()
    
class PrescribedMedicine(models.Model):
    Id = models.AutoField(primary_key=True)
    PrescriptionId = models.CharField(max_length=100)
    MedicineName = models.CharField(max_length=100)
    MedicineDescription= models.CharField(max_length=200)
    
class Appointments(models.Model):
    Id = models.AutoField(primary_key=True)
    PatientId = models.CharField(max_length=100,default='0')
    PatientName = models.CharField(max_length=100) 
    Address= models.CharField(max_length=200)
    Phone= models.CharField(max_length=50)
    pin = models.CharField(max_length=50)
    Email= models.CharField(max_length=50)
    Gender= models.IntegerField(null=True)
    AppointmentTypeId= models.IntegerField(blank=True, null=True)
    AppointmentDate=models.DateField(blank=True, null=True)
    AppointmentTime=models.TimeField(blank=True, null=True) 