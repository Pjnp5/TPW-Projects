import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AboutPageComponent } from './components/about-page/about-page.component';
import { IndexPageComponent } from './components/index-page/index-page.component';
import { ContactPageComponent } from './components/contact-page/contact-page.component';
import { NewAppointmentPageComponent } from './components/new-appointment-page/new-appointment-page.component';
import { LoginComponent } from './components/login/login.component';
import { SignupComponent } from './components/signup/signup.component';

const routes: Routes = [
  // Here we insert the routes
  { path: '', component: IndexPageComponent, pathMatch: 'full' }, // Create the base page
  { path: 'about', component: AboutPageComponent },
  { path: 'contact', component: ContactPageComponent },
  { path: 'appointment', component: NewAppointmentPageComponent },
  { path: 'login', component: LoginComponent},
  { path: 'signup', component: SignupComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
