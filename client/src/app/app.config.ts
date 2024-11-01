import { ApplicationConfig, provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { provideStore } from '@ngrx/store';
import { provideEffects } from '@ngrx/effects';
import { PromptEffects } from './store/prompt/prompt.effects';
import { provideHttpClient } from '@angular/common/http';
import { promptReducer } from './store/prompt/prompt.store';

export const appConfig: ApplicationConfig = {
  providers: [
    provideZoneChangeDetection({ eventCoalescing: true }), 
    provideRouter(routes), 
    provideAnimationsAsync(), 
    provideStore({
      'prompt': promptReducer
    }), 
    provideEffects([PromptEffects]),
    provideHttpClient()
  ]
};
