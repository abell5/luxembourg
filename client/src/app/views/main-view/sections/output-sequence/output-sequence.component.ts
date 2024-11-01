import { Component, Input, output } from '@angular/core';
import { TokenDistribution } from '../../../../model/tokenDistribution.model';
import { SelectedTokenComponent } from "./sections/selected-token/selected-token.component";
import { TokenSelectorPipe } from '../../../../pipe/TokenSelectorPipe';

@Component({
  selector: 'app-output-sequence',
  standalone: true,
  imports: [
    
    // pipes
    TokenSelectorPipe,

    // components
    SelectedTokenComponent],
  templateUrl: './output-sequence.component.html',
  styleUrl: './output-sequence.component.scss'
})
export class OutputSequenceComponent {

  protected _tokenDistribution: TokenDistribution[] = [];

  // inputs
  @Input({alias: 'tokenDistribution'})
  get tokenDistribution(): TokenDistribution[] {

    if( !this._tokenDistribution ) return []
    return this._tokenDistribution;

  }
  set tokenDistribution(tokenDistribution: TokenDistribution[] | null) {    
    
    if( !tokenDistribution ) return;
    this._tokenDistribution = tokenDistribution;
  
  }


  // events
  protected tokenClicked = output<TokenDistribution>();

}
