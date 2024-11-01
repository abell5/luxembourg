// core
import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable, of } from "rxjs";
import { Token } from "../model/token.model";
import { TokenDistribution } from "../model/tokenDistribution.model";

// environments

@Injectable({
    providedIn: 'root'
})
export class PromptAPIService {

    constructor(){}

    public get_output_sequence( prompt: string ): Observable<TokenDistribution[]> {

        const tokenDistribution: TokenDistribution[] = [
            new TokenDistribution( '0', 0, [new Token('lorem', Math.random(), false),          new Token('ipsum', Math.random(), true),        new Token('perspiciatis', Math.random(), false)] ),
            new TokenDistribution( '1', 1, [new Token('dolor', Math.random(), false),          new Token('sit', Math.random(), true),          new Token('unde', Math.random(), false)] ),
            new TokenDistribution( '2', 2, [new Token('amet', Math.random(), false),           new Token('consectetur', Math.random(), true),  new Token('omnis', Math.random(), false)] ),
            new TokenDistribution( '3', 3, [new Token('adipiscing', Math.random(), false),     new Token('elit', Math.random(), true),         new Token('iste', Math.random(), false)]   ),
            new TokenDistribution( '4', 4, [new Token('sed', Math.random(), false),            new Token('do', Math.random(), true),           new Token('natus', Math.random(), false)]   ),
            new TokenDistribution( '5', 5, [new Token('eiusmod', Math.random(), false),        new Token('tempor', Math.random(), true),       new Token('error', Math.random(), false)]  ),
            new TokenDistribution( '6', 6, [new Token('lorem', Math.random(), false),          new Token('ipsum', Math.random(), true),        new Token('perspiciatis', Math.random(), false)] ),
            new TokenDistribution( '7', 7, [new Token('dolor', Math.random(), false),          new Token('sit', Math.random(), true),          new Token('unde', Math.random(), false)] ),
            new TokenDistribution( '8', 8, [new Token('amet', Math.random(), false),           new Token('consectetur', Math.random(), true),  new Token('omnis', Math.random(), false)] ),
            new TokenDistribution( '9', 9, [new Token('adipiscing', Math.random(), false),     new Token('elit', Math.random(), true),         new Token('iste', Math.random(), false)]   ),
            new TokenDistribution( '10', 10, [new Token('sed', Math.random(), false),            new Token('do', Math.random(), true),           new Token('natus', Math.random(), false)]   ),
            new TokenDistribution( '11', 11, [new Token('eiusmod', Math.random(), false),        new Token('tempor', Math.random(), true),       new Token('error', Math.random(), false)]  ),
            new TokenDistribution( '12', 12, [new Token('lorem', Math.random(), false),          new Token('ipsum', Math.random(), true),        new Token('perspiciatis', Math.random(), false)] ),
            new TokenDistribution( '13', 13, [new Token('dolor', Math.random(), false),          new Token('sit', Math.random(), true),          new Token('unde', Math.random(), false)] ),
            new TokenDistribution( '14', 14, [new Token('amet', Math.random(), false),           new Token('consectetur', Math.random(), true),  new Token('omnis', Math.random(), false)] ),
            new TokenDistribution( '15', 15, [new Token('adipiscing', Math.random(), false),     new Token('elit', Math.random(), true),         new Token('iste', Math.random(), false)]   ),
            new TokenDistribution( '16', 16, [new Token('sed', Math.random(), false),            new Token('do', Math.random(), true),           new Token('natus', Math.random(), false)]   ),
            new TokenDistribution( '17', 17, [new Token('eiusmod', Math.random(), false),        new Token('tempor', Math.random(), true),       new Token('error', Math.random(), false)]  ),
            new TokenDistribution( '18', 18, [new Token('lorem', Math.random(), false),          new Token('ipsum', Math.random(), true),        new Token('perspiciatis', Math.random(), false)] ),
            new TokenDistribution( '19', 19, [new Token('dolor', Math.random(), false),          new Token('sit', Math.random(), true),          new Token('unde', Math.random(), false)] ),
            new TokenDistribution( '20', 20, [new Token('amet', Math.random(), false),           new Token('consectetur', Math.random(), true),  new Token('omnis', Math.random(), false)] ),
            new TokenDistribution( '21', 21, [new Token('adipiscing', Math.random(), false),     new Token('elit', Math.random(), true),         new Token('iste', Math.random(), false)]   ),
            new TokenDistribution( '22', 22, [new Token('sed', Math.random(), false),            new Token('do', Math.random(), true),           new Token('natus', Math.random(), false)]   ),
            new TokenDistribution( '23', 23, [new Token('eiusmod', Math.random(), false),        new Token('tempor', Math.random(), true),       new Token('error', Math.random(), false)]  ),
            new TokenDistribution( '24', 24, [new Token('lorem', Math.random(), false),          new Token('ipsum', Math.random(), true),        new Token('perspiciatis', Math.random(), false)] ),
            new TokenDistribution( '25', 25, [new Token('dolor', Math.random(), false),          new Token('sit', Math.random(), true),          new Token('unde', Math.random(), false)] ),
            new TokenDistribution( '26', 26, [new Token('amet', Math.random(), false),           new Token('consectetur', Math.random(), true),  new Token('omnis', Math.random(), false)] ),
            new TokenDistribution( '27', 27, [new Token('adipiscing', Math.random(), false),     new Token('elit', Math.random(), true),         new Token('iste', Math.random(), false)]   ),
            new TokenDistribution( '28', 28, [new Token('sed', Math.random(), false),            new Token('do', Math.random(), true),           new Token('natus', Math.random(), false)]   ),
            new TokenDistribution( '29', 29, [new Token('eiusmod', Math.random(), false),        new Token('tempor', Math.random(), true),       new Token('error', Math.random(), false)]  ),
            new TokenDistribution( '30', 30, [new Token('lorem', Math.random(), false),          new Token('ipsum', Math.random(), true),        new Token('perspiciatis', Math.random(), false)] ),
        ];

        return of(tokenDistribution)

    }

}