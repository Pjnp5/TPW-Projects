import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-update-appointment-page',
  templateUrl: './update-appointment-page.component.html',
  styleUrls: ['./update-appointment-page.component.css']
})
export class UpdateAppointmentPageComponent implements OnInit {

  constructor(private router: Router) { }


  ngOnInit(): void {
    let url = this.router.url.split("/").at(-1)
    console.log(url)
  }

}
