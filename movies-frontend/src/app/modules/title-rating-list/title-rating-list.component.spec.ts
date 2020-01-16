import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TitleRatingListComponent } from './title-rating-list.component';

describe('TitleRatingListComponent', () => {
  let component: TitleRatingListComponent;
  let fixture: ComponentFixture<TitleRatingListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TitleRatingListComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TitleRatingListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
