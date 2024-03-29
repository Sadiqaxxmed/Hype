import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import OutfitDetails from "./components/OutfitDetails";
import UploadOutfit from "./components/UploadOutfit";
import UpdateOutfit from "./components/UpdateOutfit";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import Home from "./components/Home";
import ProfilePage from "./components/ProfilePage";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      <Navigation isLoaded={isLoaded} />
      {isLoaded && (
        <Switch>
          <Route path="/Home" component={Home}>
          </Route>
          <Route path="/ProfilePage/:user_id" component={ProfilePage}>
          </Route>
          <Route path="/outfitDetails/:outfit_id" component={OutfitDetails}>
          </Route>
          <Route path="/UploadOutfit" component={UploadOutfit}>
          </Route>
          <Route path="/UpdateOutfits/:outfit_id" component={UpdateOutfit}>
          </Route>
          <Route path="/login" >
            <LoginFormPage />
          </Route>
          <Route path="/signup">
            <SignupFormPage />
          </Route>
        </Switch>
      )}
    </>
  );
}

export default App;
