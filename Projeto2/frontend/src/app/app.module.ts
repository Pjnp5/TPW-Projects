import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BasePageComponent } from './components/base-page/base-page.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { IndexPageComponent } from './components/index-page/index-page.component';
import { FooterComponent } from './components/footer/footer.component';
import { AboutPageComponent } from './components/about-page/about-page.component';
import { NewAppointmentPageComponent } from './components/new-appointment-page/new-appointment-page.component';
import { ContactPageComponent } from './components/contact-page/contact-page.component';
import { LoginComponent } from './components/login/login.component';
import { SignupComponent } from './components/signup/signup.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatDatepickerModule } from '@angular/material/datepicker';

@NgModule({
  declarations: [
    AppComponent,
    BasePageComponent,
    IndexPageComponent,
    FooterComponent,
    AboutPageComponent,
    NewAppointmentPageComponent,
    ContactPageComponent,
    LoginComponent,
    SignupComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FontAwesomeModule,
    FormsModule,
    ReactiveFormsModule,
    BrowserAnimationsModule,
    MatDatepickerModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
