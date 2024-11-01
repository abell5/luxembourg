import { createReducer, on } from '@ngrx/store'
import { TokenDistribution } from '../../model/tokenDistribution.model';
import { EntityState } from '@ngrx/entity';
import { adapter, selectedTokenDistributionID } from './prompt.state';
import { promptResponseGenerated } from './prompt.actions';

const initialState: EntityState<TokenDistribution> = adapter.getInitialState({
    selectedTokenDistributionID: null
});

export const promptReducer = createReducer( 

    initialState,

    on( promptResponseGenerated, (state: EntityState<TokenDistribution>, action: {type: string, promptResponse: TokenDistribution[]}) => {
        return adapter.setAll( action.promptResponse, {...state, selectedFrameId: null });
    })

)