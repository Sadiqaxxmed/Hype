import React, { useEffect, useState } from "react";
import { useHistory, useParams } from 'react-router-dom';
import { useSelector, useDispatch } from "react-redux";

import { thunkUpdateOutfits } from "../../store/outfit";

import './UpdateOutfit.css';

function UpdateOutfit(){

    const history = useHistory();
    const dispatch = useDispatch();
    const { outfit_id } = useParams();

    const outfit = useSelector(state => state.outfits.allOutfits?.[outfit_id]);

    const [image, setImage] = useState(outfit.image);
    const [description, setDescription] = useState(outfit.description);
    const [outfitPrice, setOutfitPrice] = useState(outfit.outfitPrice);
    const [catagory, setCatagory] = useState(outfit.catagory);
    const [errors, setErrors] = useState({});

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
        outfit.append('owner_id', outfit_id)

        dispatch(thunkUpdateOutfits(outfit, outfit_id));
        return history.push('/home');
    };

	return (
		<>
		<div className='UPO-Main-Div'>
            <h1 className='UPO-Upload-Title'>Update Outfit</h1>
            <div className='UPO-Upload-Div'>
            <form className="PS-Form" onSubmit={handleSubmit} method="PUT" encType="multipart/form-data">
                {errors.emptyImage ? <div className="PS-Empty-Errors">{errors.emptyImage}</div> : null}
                <input
                    type="text"
                    name="outfitImage"
                    onChange={(e) => setImage(e.target.value)}
                    value={image}
                    placeholder="Image"
                    className="UPO-Outfit-Image"
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
                    className="UPO-Outfit-Price"
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
                    className="UPO-Category-Select"
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
                    className="UPO-Outfit-Description"
                    style={{
                        height: '100px',
                        width: '550px',
                        border: '2px solid #ccc',
                        borderRadius: '10px',
                        padding: '5px',
                        paddingLeft: '10px',
                    }}
                />
                <button className="UPO-Update-Button" onClick={handleSubmit} type="submit">Update</button>
            </form>   
            </div>
		</div>		           
		</>
	);
}

export default UpdateOutfit;

