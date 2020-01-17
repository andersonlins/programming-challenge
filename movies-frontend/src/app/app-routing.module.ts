import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {TitleListComponent} from './modules/title/title-list/title-list.component';

const appRoutes: Routes = [
  { path: '', component: TitleListComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(appRoutes, {useHash: true}) ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
