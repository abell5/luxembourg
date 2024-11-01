import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SelectedTokenComponent } from './selected-token.component';

describe('SelectedTokenComponent', () => {
  let component: SelectedTokenComponent;
  let fixture: ComponentFixture<SelectedTokenComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SelectedTokenComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SelectedTokenComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
