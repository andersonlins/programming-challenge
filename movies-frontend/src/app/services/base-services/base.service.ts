import {HttpClient, HttpParams} from '@angular/common/http';
import {PaginatedResult} from './paginated-result';
import {Observable} from 'rxjs';

export class BaseService<T> {
  protected protocol: string = location.protocol;
  protected hostname: string = location.hostname;
  private api = ':8000/api/titles/';
  protected headers = new Headers(
    {
      'Content-Type': 'application/json',
      'Content-Language': 'pt-br',
      'Accept-Language': 'pt-br',
    }
  );
  protected urlBase: string;
  protected parameters: HttpParams;
  protected fullUrl: string;

  constructor(protected http: HttpClient, path: string ) {
    this.urlBase = this.getUrlBase();
    this.parameters = new HttpParams();
    this.fullUrl = this.urlBase.concat(path);
  }

  public getUrlBase(): string {
    return this.protocol.concat('//').concat(this.hostname).concat(this.api);
  }

  public clearParameter(): void {
    this.parameters = new HttpParams();
  }

  public addParameter(key: string, value: string): void {
    this.parameters = this.parameters.set(key, value);
  }

  protected getOptions(parameters?: HttpParams) {
    const options = {headers: {}, params: {}};

    options.headers = this.headers;
    if (parameters) {
      options.params = parameters;
    }

    return options;
  }

  public getAll(): Observable<T[]> {
    return this.http.get<T[]> (this.fullUrl, this.getOptions(this.parameters));
  }

  public getPaginated(): Observable<PaginatedResult<T>> {
    return this.http.get<PaginatedResult<T>>(this.fullUrl, this.getOptions(this.parameters));
  }

  public getPaginatedNext(fullUrl): Observable<PaginatedResult<T>> {
    return this.http.get<PaginatedResult<T>>(fullUrl, this.getOptions(this.parameters));
  }

  public hostMedia(): string[] {
    const urls = this.fullUrl.split('/', 3);
    const protocol = urls[0];
    const hostname = urls[2];

    return [protocol, hostname];
  }
}
