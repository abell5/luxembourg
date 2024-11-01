import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-section-template',
  standalone: false,
  templateUrl: './section-template.component.html',
  styleUrl: './section-template.component.scss'
})
export class SectionTemplateComponent {

  @Input('title') title: string = '';

} 
