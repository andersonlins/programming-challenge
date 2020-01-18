import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {BaseService} from './base-services/base.service';
import {Title} from '../models/title';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TitleService extends BaseService<Title>{
  constructor(protected http: HttpClient) {
    super(http, 'title/');
  }

  public get_by_year(): Observable<Title[]> {
    return this.http.get<Title[]>(this.fullUrl + 'get_by_year/', this.getOptions(this.parameters));
  }
}
