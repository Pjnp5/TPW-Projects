import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl } from '@angular/forms';

@Component({
  selector: 'app-new-appointment-page',
  templateUrl: './new-appointment-page.component.html',
  styleUrls: ['./new-appointment-page.component.css'],
})
export class NewAppointmentPageComponent implements OnInit {
  minDate = new Date();
  constructor(private formBuilder: FormBuilder) {}

  objects = ['cona', 'boa'];

  profileForm = this.formBuilder.group({
    department: [''],
    date: [''],
    message: [''],
  });

  saveForm() {
    console.log('Form data is: ', this.profileForm.value);
  }

  ngOnInit(): void {}
}

export class NewAppointmentPageModule {}
