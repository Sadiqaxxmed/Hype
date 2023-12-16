// TODO: CONSTANTS

const ALL_OUTFITS         = 'ALL_OUTFITS';
const SINGLE_OUTFITS       = 'SINGLE_OUTFITS';

// TODO: ACTION CREATORS

export const actionAllOutfits = (outfits) => {
    return { type: ALL_OUTFITS, outfits }
}

export const actionSingleOutfits = (outfits) => {
    return { type: SINGLE_OUTFITS, outfits }
  }

// TODO: NORMALIZE DATA

const normalizeAllOutfits = (outfits) => {
    let normalize = {};
    outfits.forEach(outfit => {
        normalize[outfit.id] = outfit;
    })
    return normalize;
}

// TODO: THUNK AC'S

export const thunkAllOutfits = () => async dispatch => {
    const response = await fetch('/api/outfits/allOutfits')

    if (response.ok) {
        const allOutfits = await response.json();
        const normalized = normalizeAllOutfits(allOutfits.outfits);
        dispatch(actionAllOutfits(normalized));
        return;
    }
}

export const thunkSingleOutfits = (outfitId) => async dispatch => {
    const response = await fetch(`/api/allOutfits/${outfitId}`);
  
    if (response.ok) {
      const outfit = await response.json();
      dispatch(actionSingleOutfits(outfit));
      return;
    } else {
      const res = await response.json();
      return { 'error' : res.error, status: res.status }
    }
}

// TODO: INITIAL SLICE STATE

const initialState = {
    allOutfits:   {},
    singleOutfits: {},
    userOutfits:  {}
}

// TODO: REDUCER

const outfitsReducer = (state = initialState, action) => {
    switch (action.type) {
        case ALL_OUTFITS:
        return { ...state, allOutfits: { ...action.outfits } }
        case SINGLE_OUTFITS:
        return { ...state, singleOutfits: { ...action.outfits } }
        default: return { ...state }
    }
}

export default outfitsReducer;