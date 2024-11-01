import { createAction, props } from "@ngrx/store";
import { Token } from "../../model/token.model";
import { TokenDistribution } from "../../model/tokenDistribution.model";

const promptKey = '[Prompt]';

export const getPromptResponse = createAction(
    `${promptKey} get prompt response`,
    props<{promptContent: string}>()
)

export const promptResponseGenerated = createAction(
    `${promptKey} prompt response generated`,
    props<{promptResponse: TokenDistribution[]}>()
)