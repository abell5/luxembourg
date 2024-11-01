import { Pipe, PipeTransform } from '@angular/core';
import { TokenDistribution } from '../model/tokenDistribution.model';
import { Token } from '../model/token.model';

@Pipe({
  name: 'tokenSelectorPipe',
  standalone: true,
})

export class TokenSelectorPipe implements PipeTransform {
  transform( tokenDistribution: TokenDistribution ): Token | null {

    for( let i = 0; i < tokenDistribution.tokens.length; i++ ){
        if( tokenDistribution.tokens[i].selected ){
            return tokenDistribution.tokens[i];
        }
    }

    return null;

  }
}