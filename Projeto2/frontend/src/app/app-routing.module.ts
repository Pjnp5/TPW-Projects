import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { IndexPageComponent } from './components/index-page/index-page.component';

const routes: Routes = [
  // Here we insert the routes
  {path: '', component: IndexPageComponent, pathMatch: "full"}, // Create the base page

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
