import { Component, OnInit } from '@angular/core';
import { AppointmentService } from 'src/app/services/appointment/appointment.service';
import { Emitter } from 'src/app/emitters/emitters';
import { ThisReceiver } from '@angular/compiler';
import { Appointment } from 'src/app/models/Appointment';

@Component({
  selector: 'app-my-appointments-page',
  templateUrl: './my-appointments-page.component.html',
  styleUrls: ['./my-appointments-page.component.css']
})
export class MyAppointmentsPageComponent implements OnInit {
  appointments: Appointment[];
  userId: any;
  userType: any;

  constructor(
    private appointmentService : AppointmentService,
  ) {
   this.appointments = []
  }


  deleteAppointment(appointmentId: any){
    console.log(appointmentId)
    this.appointmentService.deleteAppointment(appointmentId).subscribe()
    window.location.reload()
  }

  ngOnInit(): void {
    Emitter.userId.subscribe(
      u => {
        this.userId = u;
    });
    Emitter.usertype.subscribe(
      t => {
        this.userType = t;
    });
    this.appointmentService.getAllAppointments().subscribe(
      (appointments : Appointment[]) => {
        for (let a of appointments){
          if (this.userType == "patient" && a.patient == this.userId){
            this.appointments.push(a);
          }
        }
      }
    )
  }

}
