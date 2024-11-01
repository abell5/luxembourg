import { Component, output } from '@angular/core';
import { MaterialModule } from '../../../../material/material.module';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-input-prompt',
  standalone: true,
  imports: [MaterialModule, FormsModule],
  templateUrl: './input-prompt.component.html',
  styleUrl: './input-prompt.component.scss'
})
export class InputPromptComponent {

  public currentPrompt: string = '';

  // events
  public promptGenerated = output<string>();

  public submitPromptText(): void {
    this.promptGenerated.emit(this.currentPrompt);
  }

}
