import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl } from '@angular/forms';
import { Department } from 'src/app/models/Department';
import { Appointment } from 'src/app/models/Appointment';
import { DepartmentService } from 'src/app/services/department/department.service';
import { AppointmentService } from 'src/app/services/appointment/appointment.service';
import { Emitter } from 'src/app/emitters/emitters';
import { Router } from '@angular/router';


@Component({
  selector: 'app-new-appointment-page',
  templateUrl: './new-appointment-page.component.html',
  styleUrls: ['./new-appointment-page.component.css'],
})
export class NewAppointmentPageComponent implements OnInit {
  minDate = new Date();
  departments: Department[];
  is_authenticated: boolean;
  userId: any;

  constructor(
    private formBuilder: FormBuilder,
    private departmentService: DepartmentService,
    private appointmentService : AppointmentService,
    private router: Router
  ) {
    this.departments = [];
    this.is_authenticated = false;
  }

  profileForm = this.formBuilder.group({
    department: [''],
    date: [''],
    message: [''],
  });

  saveForm() {
    console.log(this.profileForm.value.department)
    if (this.profileForm.value.department != null){    
      let departmentName: any = this.profileForm.value.department;
      let date: any = this.profileForm.value.date?.toString();
      let message: any = this.profileForm.value.department;

      let data: Appointment;

      data = new Appointment(0, this.userId, departmentName, date, message)
      this.appointmentService.createAppointment(data).subscribe(r => r);
      this.router.navigate(["myappointments"]).then(() => window.location.reload());
    }
  }

  ngOnInit(): void {
    this.departmentService.getAllDepartments().subscribe(
      d => {
        this.departments = d;
      }
    );
    Emitter.isAuthenticated.subscribe(
      (auth: boolean) => {
        this.is_authenticated = auth;
      }
    );
    Emitter.userId.subscribe(
      u => {
        this.userId = u;
      }
    );
  }
}

export class NewAppointmentPageModule {}
