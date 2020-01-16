import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {BaseService} from './base-services/base.service';
import {Title} from '../models/title';

@Injectable({
  providedIn: 'root'
})
export class TitleService extends BaseService<Title>{
  constructor(protected http: HttpClient) {
    super(http, 'title/');
  }
}
