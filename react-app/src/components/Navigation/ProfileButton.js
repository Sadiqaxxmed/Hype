import React, { useState, useEffect, useRef } from "react";
import { useDispatch } from "react-redux";
import { useHistory } from "react-router-dom";
import { logout } from "../../store/session";
import OpenModalButton from "../OpenModalButton";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import profileIcon from '../../images/profileicon.png'
import ProfilePage from "../ProfilePage";
import "./ProfileButton.css";

function ProfileButton({ user }) {
  const dispatch = useDispatch();
  const history = useHistory();

  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();

  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (!ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const handleLogout = (e) => {
    e.preventDefault();
    dispatch(logout());
  };

  const ulClassName = "profile-dropdown" + (showMenu ? "" : " hidden");
  const closeMenu = () => setShowMenu(false);

  const navigateToProfilePage = (user_id) => {
    history.push(`/ProfilePage/${user_id}`)
  }

  return (
    <>
      <div onClick={openMenu}>
        <span class="material-symbols-outlined">
          menu
        </span>
      </div>
      <img src={user?.profile_image} className="NV-Profile-Icon" onClick={() => navigateToProfilePage(user.id)}></img>
      <ul className={ulClassName} ref={ulRef}>
        {user ? (
          <>
            <div className="NV-Profile-Username">
              <img src={user.profile_image}></img>
              <p>{user.username}</p>
            </div>
            <div className="NV-Profile-Outfit-Logout">
            <p> Upload Outfit </p>
            <button onClick={handleLogout}>Log Out</button>

            </div>
          </>
        ) : (
          <>
            <OpenModalButton
              buttonText="Log In"
              onItemClick={closeMenu}
              modalComponent={<LoginFormModal />}
            />

            <OpenModalButton
              buttonText="Sign Up"
              onItemClick={closeMenu}
              modalComponent={<SignupFormModal />}
            />
          </>
        )}
      </ul>
    </>
  );
}

export default ProfileButton;
