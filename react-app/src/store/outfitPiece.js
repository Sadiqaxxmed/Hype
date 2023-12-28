// TODO: CONSTANTS

const ALL_OUTFIT_PIECES = 'ALL_OUTFIT_PIECES';
const CREATE_OUTFIT_PIECES = 'CREATE_OUTFIT_PIECES';

// TODO: ACTION CREATORS

export const actionAllOutfitPieces = (outfitPieces) => {
    return { type: ALL_OUTFIT_PIECES, outfitPieces }
}

export const actionCreateOutfitPieces = (outfitPiece) => {
    return { type: CREATE_OUTFIT_PIECES, outfitPiece }
}


// TODO: NORMALIZE DATA

const normalizeAllOutfitPieces = (outfitPieces) => {
    let normalize = {};
    outfitPieces.forEach(outfitPiece => {
        normalize[outfitPiece.id] = outfitPiece;
    })
    return normalize;
}

// TODO: THUNK AC'S

export const thunkAllOutfitPieces = (outfit_id) => async dispatch => {
    const response = await fetch(`/api/pieces/outfitDetails/${outfit_id}`)

    if (response.ok) {
        const allOutfitPieces = await response.json();
        const normalized = normalizeAllOutfitPieces(allOutfitPieces.pieces);
        dispatch(actionAllOutfitPieces(normalized));
        return;
    }
}

export const thunkCreateOutfitPieces = (outfitPiece) => async dispatch => {
    const response = await fetch('/api/outfitPieces/createOutfitPiece', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(outfitPiece)
    })

    if (response.ok) {
        const newOutfitPiece = await response.json();
        dispatch(actionCreateOutfitPieces(newOutfitPiece));
        return;
    }
}


// TODO: INITIAL SLICE STATE

const initialState = {
    allOutfitPieces: {}
};

// TODO: REDUCER

const outfitPieceReducer = (state = initialState, action) => {
    switch (action.type) {
        case ALL_OUTFIT_PIECES:
            return { ...state, allOutfitPieces: { ...action.outfitPieces } }
        case CREATE_OUTFIT_PIECES:
            return { ...state, allOutfitPieces: { ...state.allOutfitPieces, [action.outfitPiece.id]: action.outfitPiece } }
        default:
            return state;
    }
}

export default outfitPieceReducer;