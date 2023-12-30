import React, { useEffect, useState } from "react";
import { useHistory } from 'react-router-dom';
import { useSelector, useDispatch } from "react-redux";

import { thunkCreateOutfits } from "../../store/outfit";

import './UploadOutfit.css';

function UploadOutfit(){

    const history = useHistory();
    const dispatch = useDispatch();

    const [image, setImage] = useState('');
    const [description, setDescription] = useState('');
    const [outfitPrice, setOutfitPrice] = useState(null);
    const [catagory, setCatagory] = useState('');
    const [errors, setErrors] = useState({});

    const user_id = useSelector(state => state.session.user?.id);

    const handleOutfit = async (e) => {

        e.preventDefault();
        let err = {}
    
        if (image.length <= 0) {
            err.emptyImage = 'Empty field cannot be submitted.'
        }

        if (description.length <= 0) {
            err.emptyDescription = 'Empty field cannot be submitted.'
        }

        if (outfitPrice <= 0) {
            err.emptyOutfitPrice = 'Empty field cannot be submitted.'
        }
    
        if (Object.values(err).length) return setErrors(err)
    
        const outfit = new FormData();
    
        outfit.append('image', image)
        outfit.append('description', description)
        outfit.append('outfitPrice', outfitPrice)
        outfit.append('catagory', catagory)
        outfit.append('owner_id', user_id)

        dispatch(thunkCreateOutfits(outfit, user_id));
        return history.push('/home');
    };

    const handlePieces = async (e) => {
        e.preventDefault();
    };

    const handleSubmit = async (e) => { 
        e.preventDefault();
        handleOutfit();
        handlePieces();
    }


	return (
		<>
		<div className='UO-Main-Div'>


            <h1 className='UO-Upload-Title'>Upload Outfit</h1>
            <div class="UO-Nav-border"></div>
            <div class="UO-Side-border"></div>
            <h2 className='UO-Outfit-Details'>Outfit Details</h2>
            <h2 className='UO-Outfit-Pieces'>Outfit Pieces</h2>
            <button className="UO-Upload-Button" onClick={handleSubmit} type="submit">Upload</button>


            <div className='UO-Upload-Div'>

            <form className="Upload-Outfit-Form" onSubmit={handleOutfit} method="POST" encType="multipart/form-data">
                {errors.emptyImage ? <div className="PS-Empty-Errors">{errors.emptyImage}</div> : null}
                <input
                    type="text"
                    name="outfitImage"
                    onChange={(e) => setImage(e.target.value)}
                    value={image}
                    placeholder="Outfit Image"
                    className="UO-Outfit-Image"
                    style={{
                        height: '30px',
                        width: '95%',
                        border: '2px solid #ccc',
                        borderRadius: '10px',
                        padding: '5px',
                        paddingLeft: '10px',
                    }}
                />
                {errors.emptyOutfitPrice ? <div className="PS-Empty-Errors">{errors.emptyOutfitPrice}</div> : null}
                <input
                    type="number"
                    name="outfitPrice"
                    onChange={(e) => setOutfitPrice(e.target.value)}
                    value={outfitPrice}
                    placeholder="Outfit Price"
                    className="UO-Outfit-Price"
                    style={{
                        height: '30px',
                        width: '95%',
                        border: '2px solid #ccc',
                        borderRadius: '10px',
                        padding: '5px',
                        paddingLeft: '10px',
                    }}
                />
                <input
                    type="text"
                    name="category"
                    onChange={(e) => setCatagory(e.target.value)}
                    value={catagory}
                    placeholder="Category"
                    className="UO-Category-Select"
                    style={{
                        height: '30px',
                        width: '95%',
                        border: '2px solid #ccc',
                        borderRadius: '10px',
                        padding: '5px',
                        paddingLeft: '10px',
                    }}
                />
                {errors.emptyDescription ? <div className="PS-Empty-Errors">{errors.emptyDescription}</div> : null}
                <textarea
                    type="text"
                    name="description"
                    onChange={(e) => setDescription(e.target.value)}
                    value={description}
                    placeholder="Give your auidence a feel of this outfit!"
                    className="UO-Outfit-Description"
                    style={{
                        height: '100px',
                        width: '95%',
                        border: '2px solid #ccc',
                        borderRadius: '10px',
                        padding: '5px',
                        paddingLeft: '10px',
                    }}
                />
            </form>

            <form className="Upload-Pieces-Form" onSubmit={handlePieces} method="POST" encType="multipart/form-data">
                <input
                    type="text"
                    name="pieceName"
                    // onChange={(e) => setCatagory(e.target.value)}
                    // value={catagory}
                    placeholder="Piece Name"
                    className="UO-Piece-Name"
                    style={{
                        height: '30px',
                        width: '95%',
                        border: '2px solid #ccc',
                        borderRadius: '10px',
                        padding: '5px',
                        paddingLeft: '10px',
                    }}
                />
                <input
                    type="number"
                    name="piecePrice"
                    // onChange={(e) => setOutfitPrice(e.target.value)}
                    // value={outfitPrice}
                    placeholder="Piece Price"
                    className="UO-Piece-Price"
                    style={{
                        height: '30px',
                        width: '95%',
                        border: '2px solid #ccc',
                        borderRadius: '10px',
                        padding: '5px',
                        paddingLeft: '10px',
                    }}
                />
                <input
                    type="text"
                    name="link"
                    // onChange={(e) => setCatagory(e.target.value)}
                    // value={catagory}
                    placeholder="Link"
                    className="UO-Piece-Link"
                    style={{
                        height: '30px',
                        width: '95%',
                        border: '2px solid #ccc',
                        borderRadius: '10px',
                        padding: '5px',
                        paddingLeft: '10px',
                    }}
                />
                <input
                    type="text"
                    name="pieceImage"
                    // onChange={(e) => setImage(e.target.value)}
                    // value={image}
                    placeholder="Piece Image"
                    className="UO-Piece-Image"
                    style={{
                        height: '30px',
                        width: '95%',
                        border: '2px solid #ccc',
                        borderRadius: '10px',
                        padding: '5px',
                        paddingLeft: '10px',
                    }}
                />
            </form>
            </div>

		</div>		           
		</>
	);
}

export default UploadOutfit;

