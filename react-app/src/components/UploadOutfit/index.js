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

    const handleSubmit = async (e) => {

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

	return (
		<>
		<div className='UO-Main-Div'>
            <h1 className='UO-Upload-Title'>Upload Outfit</h1>
            <div className='UO-Upload-Div'>
            <form className="PS-Form" onSubmit={handleSubmit} method="POST" encType="multipart/form-data">
                {errors.emptyImage ? <div className="PS-Empty-Errors">{errors.emptyImage}</div> : null}
                <input
                    type="text"
                    name="outfitImage"
                    onChange={(e) => setImage(e.target.value)}
                    value={image}
                    placeholder="Image"
                    className="UO-Outfit-Image"
                    style={{
                        height: '30px',
                        width: '550px',
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
                    placeholder="Price"
                    className="UO-Outfit-Price"
                    style={{
                        height: '30px',
                        width: '550px',
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
                        width: '550px',
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
                        width: '550px',
                        border: '2px solid #ccc',
                        borderRadius: '10px',
                        padding: '5px',
                        paddingLeft: '10px',
                    }}
                />
                <button className="UO-Upload-Button" onClick={handleSubmit} type="submit">Upload</button>
            </form>   
            </div>
		</div>		           
		</>
	);
}

export default UploadOutfit;

