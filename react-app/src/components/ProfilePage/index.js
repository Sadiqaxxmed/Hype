import React from "react";
import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from 'react-router-dom';

import './ProfilePage.css';

function ProfilePage(){
    const user = useSelector(state => state.session.user);
    console.log("USER: ",user);

    return (

        <div className="PP-Main-Div">

        <div className="PP-Profile-Card">
        <img src={user?.profile_image} className="PP-Profile-Icon"></img>
        <div className="PP-Profile-Info">
            <p className="PP-Username">{user?.username}</p>
            <p className="PP-User-Subscribers">150 Subscribers</p>
            <p className="PP-User-Bio">{user?.bio}</p>
       </div>
        </div>
        </div>
    )
}

export default ProfilePage;
