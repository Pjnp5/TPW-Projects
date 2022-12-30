import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BasePageComponent } from './components/base-page/base-page.component';

const routes: Routes = [
  // Here we insert the routes
  {path: '', component: BasePageComponent, pathMatch: "full"}, // Create the base page

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
