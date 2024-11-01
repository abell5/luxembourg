import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SectionTemplateComponent } from './section-template.component';

describe('SectionTemplateComponent', () => {
  let component: SectionTemplateComponent;
  let fixture: ComponentFixture<SectionTemplateComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SectionTemplateComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SectionTemplateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
