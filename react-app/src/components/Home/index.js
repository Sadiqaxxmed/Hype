import React from "react";
import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { thunkAllOutfits } from "../../store/outfit";

import OpenModalButton from "../OpenModalButton";
import OutfitDetails from "../OutfitDetails";
import UpdateOutfit from "../UpdateOutfit";
import DeleteOutfit from "../DeleteOutfit";

import './home.css'

function Home(){

    const dispatch = useDispatch();
    const history = useHistory();

    const users = useSelector(state => state.session.user?.id);
    const outfits = Object.values(useSelector(state => state.outfits.allOutfits));

    const [menuOpen, setMenuOpen] = useState(false);
    const [outfitId, setOutfitId] = useState(null);



    const navigateToUpdateOutfit = (outfit_id) => {
        history.push(`/updateOutfits/${outfit_id}`)
    }

    const navigateToOutfitDetails = (outfit_id) => {    
        history.push(`/outfitDetails/${outfit_id}`)
    }

    function handleMenu(id) {
        if (!menuOpen && id) {
            setMenuOpen(true); 
            setOutfitId(id); 
        } else {
            setMenuOpen(false);
            setOutfitId(null);
        }
    }
    

    useEffect(() => {   
        dispatch(thunkAllOutfits())
    }, [dispatch])

    return (
        <div className="HM-Main-Div">
        {outfits.map((outfit) => (
            <div className="HM-Outfits-Div">
            <img className="HM-Outfit-Pic" src={outfit.image} alt="profile"></img>
            <div className="HM-Outfit-Info-Div">
                <i
                    class="fa-solid fa-ellipsis fa-xl HM-Outfit-Menu-Icon"
                    onClick={(e) => handleMenu(outfit.id)}
                ></i>
                {menuOpen && outfitId === outfit.id && (
                <div className="HM-Outfit-Menu-Div">
                    <div className="HM-Outfit-Update-Div">
                        <OpenModalButton
                        className="HM-Outfit-Update HM-Outfit-Update-Text"
                        buttonText="Update Outfit"
                        onButtonClick={() => navigateToUpdateOutfit(outfit.id)}
                        />
                    </div>
                    <div className="HM-Outfit-Delete-Div">
                        <OpenModalButton
                        className="HM-Outfit-Delete HM-Outfit-Delete-Text"
                        buttonText="Delete Outfit"
                        onButtonClick={""}
                        modalComponent={<DeleteOutfit outfit_id={outfit.id}/>}
                        />
                    </div>     
                </div>
                )}
                <p className="HM-Outfit-Review">2.9 <i class="fa-solid fa-star"></i></p>
                <div className="HM-OutfitDetail-Click" onClick={() => navigateToOutfitDetails(outfit.id)}></div>
                <div className="HM-Profile-Card">
                    <img class="HM-Profile-Image" src="data:image/jpeg;base64,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" alt="profile" />
                    <p className="HM-Profile-Name">Lil Yachty</p>
                </div>
            </div>

        </div>
        ))}

        </div>
    )
}

export default Home;