import { Component, Input, Output, output } from '@angular/core';
import { Token } from '../../../../../../model/token.model';
import { ColorScaleService } from '../../../../services/colorScale.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-selected-token',
  standalone: true,
  imports: [ CommonModule ],
  templateUrl: './selected-token.component.html',
  styleUrl: './selected-token.component.scss'
})
export class SelectedTokenComponent {

  @Input('token') token: Token | null = null;

  constructor( public colorScaleService: ColorScaleService ){}

}
