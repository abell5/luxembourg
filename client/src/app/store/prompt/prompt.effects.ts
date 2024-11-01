import { Injectable } from "@angular/core";
import { Actions, createEffect, ofType } from "@ngrx/effects";
import { getPromptResponse, promptResponseGenerated } from "./prompt.actions";
import { map, switchMap } from "rxjs";
import { PromptAPIService } from "../../api/prompt.api";
import { Token } from "../../model/token.model";
import { TokenDistribution } from "../../model/tokenDistribution.model";

@Injectable()
export class PromptEffects {

    constructor( private actions$: Actions, private promptAPIService: PromptAPIService ){}

    public _getPromptResponse$ = createEffect(() => 

        this.actions$.pipe(
            ofType(getPromptResponse),
            switchMap( (action: {type: string, promptContent: string} ) =>  {
                
                return this.promptAPIService.get_output_sequence(action.promptContent).pipe(
                    map( (tokenDistribution: TokenDistribution[]) =>{
                        return promptResponseGenerated({promptResponse: tokenDistribution})
                    })
                )
            })
        ), {dispatch: true}
    );

}