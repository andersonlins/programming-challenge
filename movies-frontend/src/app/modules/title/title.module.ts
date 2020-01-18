import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {TitleListComponent} from './title-list/title-list.component';
import {TitleRatingListComponent} from './title-rating-list/title-rating-list.component';
import {BrowserModule} from '@angular/platform-browser';
import {AppRoutingModule} from '../../app-routing.module';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {LayoutModule} from '@angular/cdk/layout';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatButtonModule} from '@angular/material/button';
import {MatSidenavModule} from '@angular/material/sidenav';
import {MatIconModule} from '@angular/material/icon';
import {MatListModule} from '@angular/material/list';
import {MatFormFieldModule, MatInputModule, MatPaginatorModule, MatSelectModule, MatTableModule} from '@angular/material';
import {FormsModule} from '@angular/forms';
import {HttpClientModule} from '@angular/common/http';
import {FlexLayoutModule} from '@angular/flex-layout';


@NgModule({
  declarations: [
    TitleListComponent,
    TitleRatingListComponent
  ],
    imports: [
        CommonModule,
        HttpClientModule,
        BrowserModule,
        AppRoutingModule,
        BrowserAnimationsModule,
        LayoutModule,
        MatToolbarModule,
        MatButtonModule,
        MatSidenavModule,
        MatIconModule,
        MatListModule,
        MatPaginatorModule,
        MatFormFieldModule,
        MatSelectModule,
        FormsModule,
        MatTableModule,
        FlexLayoutModule,
        MatInputModule
    ]
})
export class TitleModule { }
