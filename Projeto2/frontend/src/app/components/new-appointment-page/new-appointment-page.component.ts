import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl } from '@angular/forms';

@Component({
  selector: 'app-new-appointment-page',
  templateUrl: './new-appointment-page.component.html',
  styleUrls: ['./new-appointment-page.component.css'],
})
export class NewAppointmentPageComponent implements OnInit {
  constructor(private formBuilder: FormBuilder) {}

  profileForm = this.formBuilder.group({
    department: [''],
    date: [''],
    message: [''],
  });

  ngOnInit(): void {}
}

export class NewAppointmentPageModule {}
