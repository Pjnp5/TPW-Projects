import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AboutPageComponent } from './components/about-page/about-page.component';
import { IndexPageComponent } from './components/index-page/index-page.component';
import { ContactPageComponent } from './components/contact-page/contact-page.component'

const routes: Routes = [
  // Here we insert the routes
  {path: '', component: IndexPageComponent, pathMatch: "full"}, // Create the base page
  {path: 'about', component: AboutPageComponent},
  {path: 'contact', component: ContactPageComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
