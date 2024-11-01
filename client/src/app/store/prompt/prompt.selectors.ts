import { createFeatureSelector, createSelector } from "@ngrx/store";
import { adapter, TokenDistributionState } from "./prompt.state";

// import { FrameState, adapter } from "./frames.state";

export const promptFeatureSelected = createFeatureSelector<TokenDistributionState>('prompt');

// export const getSelectedFrameId = (state: FrameState) => state.selectedFrameId;

// selectors
export const selectTokenDistribution = createSelector(
    promptFeatureSelected,
    adapter.getSelectors().selectAll
)

// // export const selectVideoEntities = createSelector( 
// //     videosFeatureSelector,  
// //     adapter.getSelectors().selectEntities
// // );

// // export const selectCurrentVideoID = createSelector( 
// //     videosFeatureSelector,  
// //     getSelectedVideoId
// // ); 

// // // TODO: define types 
// // export const selectCurrentVideo = createSelector( 
// //     selectVideoEntities,  
// //     selectCurrentVideoID,
// //     ( videoEntities: any, videoID: string | null ) => videoID && videoEntities[videoID]
// // ); 