import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OutputSequenceComponent } from './output-sequence.component';

describe('OutputSequenceComponent', () => {
  let component: OutputSequenceComponent;
  let fixture: ComponentFixture<OutputSequenceComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [OutputSequenceComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(OutputSequenceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
