import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { thunkDeleteOutfits } from "../../store/outfit";

import './DeleteOutfit.css'

import { useModal } from "../../context/Modal";


const DeleteOutfit = ({outfit_id}) => {

    const dispatch = useDispatch();
    const {closeModal} = useModal()    
    console.log('OUTFIT ID:', outfit_id)
    const handleDelete = (e) => {
        e.preventDefault();
        dispatch(thunkDeleteOutfits({outfit_id}))
        closeModal()
    }

    return(
        <div className='HM-Delete-Main-Div'>
            <h1 className="HM-Delete-Title">Are you sure you want to delete this outfit?</h1>
            <div className="HM-Delete-Buttons">
                <div className="HM-Cancel-Button" onClick={() => closeModal()}>Cancel</div>
                <div className="HM-Delete-Button" onClick={handleDelete}>Delete</div>
            </div>
        </div>
    )
}

export default DeleteOutfit