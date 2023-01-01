import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-new-appointment-page',
  templateUrl: './new-appointment-page.component.html',
  styleUrls: ['./new-appointment-page.component.css'],
})
export class NewAppointmentPageComponent implements OnInit {
  form: any[] = [];
  input1Control = new FormControl('');
  input2Control = new FormControl('');
  timeControl = new FormControl('');

  constructor() {}

  ngOnInit(): void {
    this.form = [
      { label: 'department', control: 'control1' },
      { label: 'date', control: 'control2' },
      { label: 'message', control: 'control3' },
    ];
  }
}

export class NewAppointmentPageModule {}
