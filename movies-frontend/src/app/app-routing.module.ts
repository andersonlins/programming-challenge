import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {TitleListComponent} from './modules/title/title-list/title-list.component';
import {TitleRatingListComponent} from './modules/title/title-rating-list/title-rating-list.component';


const appRoutes: Routes = [
  { path: 'movies', component: TitleListComponent },
  { path: 'movies-rating', component: TitleRatingListComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(appRoutes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
