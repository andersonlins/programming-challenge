import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {BaseService} from './base-services/base.service';
import {Rating} from '../models/rating';

@Injectable({
  providedIn: 'root'
})
export class RatingService extends BaseService<Rating>{
  constructor(protected http: HttpClient) {
    super(http, 'rating/');
  }
}
