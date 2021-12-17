import { Component, OnInit } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import { SharedService } from '../shared.service';
import { appointment } from '../shared.service';

@Component({
  selector: 'appointments',
  templateUrl: './appointments.component.html',
  styleUrls: ['./appointments.component.css']
})

export class AppointmentsComponent implements OnInit {
  
  AppointmentsList : appointment[]=[];
  
  columnsToDisplay:string[]=['Id','PatientId','PatientName','Phone','pin','Address',
  'AppointmentDate','AppointmentTime','AppointmentTypeId','Email','Gender'];

  datasource = new MatTableDataSource<appointment>(this.AppointmentsList);


  constructor(private service:SharedService) { }

  ngOnInit() {
    this.getAppointments();
  }

  public getAppointments(){
    let repo= this.service.getAppointmentsList();
    repo.subscribe(data=>this.datasource.data = data as appointment[])
      console.log(this.datasource);
  }

}
