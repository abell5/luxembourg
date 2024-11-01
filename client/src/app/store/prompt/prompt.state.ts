import { EntityAdapter, EntityState, createEntityAdapter } from "@ngrx/entity";
import { TokenDistribution } from "../../model/tokenDistribution.model";

export interface TokenDistributionState extends EntityState<TokenDistribution> {
    selectedTokenDistributionID: string | null;
}

// Defining the adapter
export function selectedTokenDistributionID( tokenDistribution: TokenDistribution ): string {
    return tokenDistribution.id;
}

export function sortByPosition(tokenDistributionA: TokenDistribution, tokenDistributionB: TokenDistribution): number {
    return tokenDistributionA.position - tokenDistributionB.position;
}

export const adapter: EntityAdapter<TokenDistribution> = createEntityAdapter<TokenDistribution>({
    selectId: selectedTokenDistributionID,
    sortComparer: sortByPosition
}); 