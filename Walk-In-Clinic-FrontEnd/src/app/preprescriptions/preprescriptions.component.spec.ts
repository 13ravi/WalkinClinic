import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PreprescriptionsComponent } from './preprescriptions.component';

describe('PreprescriptionsComponent', () => {
  let component: PreprescriptionsComponent;
  let fixture: ComponentFixture<PreprescriptionsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PreprescriptionsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PreprescriptionsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
