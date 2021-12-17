import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface appointment{
  Id:number,
  PatientId:number,
  PatientName:string,
  Phone:string,
  pin:string
  Address:string
  AppointmentDate:string,
  AppointmentTime:string,
  AppointmentTypeId:number,
  Email:string,
  Gender:string
}

@Injectable({
  providedIn: 'root'
})

export class SharedService {
readonly APIUrl = "http://127.0.0.1:8000";
readonly PhotoUrl = "http://127.0.0.1:8000/media/";

  constructor(private http:HttpClient) { }

  getPatientList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl + '/patients/');
  }

  addPatient(val:any){
    return this.http.post(this.APIUrl + '/patients/',val);
  }

  updatePatient(val:any){
    return this.http.put(this.APIUrl + '/patients/',val);
  }

  deletePatient(val:any){
    return this.http.delete(this.APIUrl + '/patients/'+val);
  }

  getStaffList():Observable<any[]>{
    return this.http.get<any[]>(this.APIUrl+'/staff/');
  }

  addStaff(val:any){
    return this.http.post(this.APIUrl + '/staff/',val);
  }

  updateStaff(val:any){
    return this.http.put(this.APIUrl + '/staff/',val);
  }

  deleteStaff(val:any){
    return this.http.delete(this.APIUrl + '/staff/'+val);
  }

  UploadPhoto(val:any){
    return this.http.post(this.APIUrl+'/SaveFile',val);
  }

  getAppointmentsList():Observable<appointment[]>{
    return this.http.get<appointment[]>(this.APIUrl + '/appointments/');
  }

  addAppointment(val:any){
    return this.http.post(this.APIUrl + '/appointments/',val);
  }

  updateAppointment(val:any){
    return this.http.put(this.APIUrl + '/appointments/',val);
  }

  deleteAppointment(val:any){
    return this.http.delete(this.APIUrl + '/appointments/'+val);
  }



}