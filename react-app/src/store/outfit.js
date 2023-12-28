// TODO: CONSTANTS

const ALL_OUTFITS           = 'ALL_OUTFITS';
const SINGLE_OUTFITS        = 'SINGLE_OUTFITS';
const USER_OUTFITS          = 'USER_OUTFITS';
const CREATE_OUTFITS        = 'CREATE_OUTFITS';
const UPDATE_OUTFITS        = 'UPDATE_OUTFITS';
const DELETE_OUTFITS        = 'DELETE_OUTFITS';

// TODO: ACTION CREATORS

export const actionAllOutfits = (outfits) => {
    return { type: ALL_OUTFITS, outfits }
}

export const actionSingleOutfits = (outfits) => {
    return { type: SINGLE_OUTFITS, outfits }
}

export const actionUserOutfits = (outfits) => {
    return { type: USER_OUTFITS, outfits }
}

export const actionCreateOutfits = (outfit) => {
    return { type: CREATE_OUTFITS, outfit }
}

export const actionUpdateOutfits = (outfit) => {
    return { type: UPDATE_OUTFITS, outfit }
}

export const actionDeleteOutfits = (outfit) => {
    return { type: DELETE_OUTFITS, outfit }
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

export const thunkUserOutfits = (userId) => async dispatch => {
    const response = await fetch(`/api/outfits/userOutfits/${userId}`);

    if (response.ok) {
        const allUseroutfits = await response.json();
        const normalized = normalizeAllOutfits(allUseroutfits.outfits);
        dispatch(actionUserOutfits(normalized));
        return;
    }
}

export const thunkCreateOutfits = (outfit, user_id) => async (dispatch) => {
    const response = await fetch(`/api/outfits/uploadOutfit/${user_id}`, {
        method: 'POST',
        body: outfit
    })

    if (response.ok) {
        const outfit = await response.json();
        dispatch(actionCreateOutfits(outfit));
        return;
    }
}

export const thunkUpdateOutfits = (outfit, outfit_id) => async (dispatch) => {
    const response = await fetch(`/api/outfits/updateOutfits/${outfit_id}`, {
        method: 'PUT',
        body: outfit
    })

    if (response.ok) {
        const outfit = await response.json();
        dispatch(actionUpdateOutfits(outfit));
        return;
    }
}

export const thunkDeleteOutfits = ({outfit_id}) => async (dispatch) => {
    const response = await fetch(`/api/outfits/deleteOutfits/${outfit_id}`, { method: 'DELETE' })

    if (response.ok) {
        const outfit = await response.json();
        dispatch(actionDeleteOutfits(outfit));
        return;
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
        case USER_OUTFITS:
        return { ...state, userOutfits: { ...action.outfits } }
        case CREATE_OUTFITS:
        return { ...state, createOutfits: { ...action.outfits } }
        case UPDATE_OUTFITS:
        return { ...state, updateOutfits: { ...action.outfits } }
        case DELETE_OUTFITS:
        return { ...state, deleteOutfits: { ...action.outfits } }
        default: return { ...state }
    }
}

export default outfitsReducer;