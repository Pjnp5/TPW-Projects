import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AboutPageComponent } from './components/about-page/about-page.component';
import { IndexPageComponent } from './components/index-page/index-page.component';
import { ContactPageComponent } from './components/contact-page/contact-page.component';
import { NewAppointmentPageComponent } from './components/new-appointment-page/new-appointment-page.component';
import { LoginComponent } from './components/login/login.component';
import { SignupComponent } from './components/signup/signup.component';
import { MyAppointmentsPageComponent } from './components/my-appointments-page/my-appointments-page.component';
import { UpdateAppointmentPageComponent } from './components/update-appointment-page/update-appointment-page.component';
import { MyPrescriptionsPageComponent } from './components/my-prescriptions-page/my-prescriptions-page.component';
import { DepartmentsPageComponent } from './components/departments-page/departments-page.component';

const routes: Routes = [
  // Here we insert the routes
  { path: '', component: IndexPageComponent, pathMatch: 'full' }, // Create the base page
  { path: 'about', component: AboutPageComponent },
  { path: 'contact', component: ContactPageComponent },
  { path: 'appointment', component: NewAppointmentPageComponent },
  { path: 'myappointments', component: MyAppointmentsPageComponent},
  { path: 'myappointments/updateappointment/:id', component: UpdateAppointmentPageComponent},
  { path: 'departments', component: DepartmentsPageComponent},
  { path: 'myprescriptions', component: MyPrescriptionsPageComponent},
  { path: 'login', component: LoginComponent},
  { path: 'signup', component: SignupComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
