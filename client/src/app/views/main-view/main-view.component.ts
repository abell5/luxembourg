import { Component, inject, OnInit } from '@angular/core';
import { MaterialModule } from '../../material/material.module';
import { InputPromptComponent } from './sections/input-prompt/input-prompt.component';
import { Store } from '@ngrx/store';
import { getPromptResponse } from '../../store/prompt/prompt.actions';
import { Observable } from 'rxjs';
import { TokenDistribution } from '../../model/tokenDistribution.model';
import { selectTokenDistribution } from '../../store/prompt/prompt.selectors';
import { OutputSequenceComponent } from './sections/output-sequence/output-sequence.component';
import { CommonModule } from '@angular/common';
import { DistributionViewComponent } from "./sections/distribution-view/distribution-view.component";
import { ToolbarComponent } from "./sections/toolbar/toolbar.component";
import { TemplatesModule } from '../../templates/templates.module';

@Component({
  selector: 'app-main-view',
  standalone: true,
  imports: [

    // modules
    MaterialModule,
    CommonModule,
    TemplatesModule,


    // components
    InputPromptComponent,
    OutputSequenceComponent,
    DistributionViewComponent,
    ToolbarComponent
],
  templateUrl: './main-view.component.html',
  styleUrl: './main-view.component.scss'
})
export class MainViewComponent implements OnInit {

  // Observables
  public promptResponse$!: Observable<TokenDistribution[]>;

  // Store
  private readonly store: Store = inject(Store);

  ngOnInit(): void {
    this.promptResponse$ = this.store.select( selectTokenDistribution );
  }
 
  public newPromptCreated( promptContent: string ): void {
    this.store.dispatch( getPromptResponse({ promptContent }));
  }

  public tokenClicked( tokenDistribution: TokenDistribution ): void {
    console.log('Token distribution: ', tokenDistribution);
  }


}
