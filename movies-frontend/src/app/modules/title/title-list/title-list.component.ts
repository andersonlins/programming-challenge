import {AfterViewInit, Component, OnInit, ViewChild} from '@angular/core';
import {MatPaginator, MatSort, MatTableDataSource, PageEvent} from '@angular/material';
import {Title} from '../../../models/title';
import {TitleService} from '../../../services/title.service';
import {Utils} from '../../../services/base-services/utils';

@Component({
  selector: 'app-title-list',
  templateUrl: './title-list.component.html',
  styleUrls: ['./title-list.component.scss']
})

export class TitleListComponent implements OnInit, AfterViewInit {

  @ViewChild(MatPaginator, {static: true})
  public paginator: MatPaginator;

  @ViewChild(MatSort, {static: true})
  sort: MatSort;

  public pageEvent = PageEvent;

  public dataSource: MatTableDataSource<any> = new MatTableDataSource();
  public resultList: Title[] = [];

  public genreFilter = '';
  public yearFilter;

  constructor(public service: TitleService) { }

  ngOnInit() {
    this.paginator.pageIndex = 0;
    this.paginator.pageSize = 10;
    this.paginator.pageSizeOptions = [10, 20, 30, 40, 50];
  }

  ngAfterViewInit(): void {
    this.retrieve();
  }

  public search() {
    this.paginator.pageIndex = 0;
    this.retrieve();
  }

  public retrieve(): void {
    this.service.clearParameter();
    this.service.addParameter('limit', String(this.paginator.pageSize));
    this.service.addParameter('offset', String(Utils.getOffset(this.paginator.pageIndex, this.paginator.pageSize)));
    this.addParametersFilters(this.service);

    this.dataSource = new MatTableDataSource(this.resultList);

    if (this.yearFilter) {
      this.service.get_by_year().subscribe(
        (response ) => {
          this.resultList = response;
          this.paginator.length = response.length ? response.length : 10;
          this.dataSource = new MatTableDataSource(this.resultList);
        },
        ex => {
          console.log(ex);
        });
    } else {
      this.service.getPaginated().subscribe(
        (response ) => {
          this.resultList = response.results;
          this.paginator.length = response.count;
          this.dataSource = new MatTableDataSource(this.resultList);
        },
        ex => {
          console.log(ex);
        }
      );
    }
  }

  addParametersFilters(serviceFilter): void {
    if (this.genreFilter) {
      serviceFilter.addParameter('genres', String(this.genreFilter));
    }

    if (this.yearFilter && this.yearFilter > 0) {
      serviceFilter.addParameter('year', String(this.yearFilter));
    }
  }

  getDisplayedColumns(): string[] {
    return ['tconst', 'primary_title', 'original_title', 'type', 'is_adult', 'start_year', 'end_year', 'genres', 'average_rating'];
  }

}
