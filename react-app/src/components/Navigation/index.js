import React from 'react';
import reactRouterDom, { NavLink } from 'react-router-dom';
import { Link } from 'react-router-dom/cjs/react-router-dom.min';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import hypeLogo from '../../images/hypeicon.png'
import './Navigation.css';

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);
	const user_id = useSelector(state => state.session.user?.id);


	return (
		<>
		<div className='NV-Main-Div'>

		<div className='NV-Left-Div'>	
		<div className='NV-Menu-Left-Options'>
			<img src={hypeLogo} alt='hype logo' className='NV-Logo'></img>		
		</div>

		<div className='NV-Menu-Right-Options'>

			<NavLink to='/Home' className="NavLink" exact={true}>
				<div className='NV-Menu-Options'>
					Home
				</div>
			</NavLink>

			<div className='NV-Menu-Options'>
				Browse
			</div>

				<NavLink to={`/uploadOutfit/${user_id}`} className="NavLink" exact={true}>
					<div className='NV-Menu-Options'>
						Upload
					</div>					
				</NavLink>

		</div>
		</div>

		<div className='NV-Right-Div'>
			<div>
  				<input className='NV-Search-Input' type='text' placeholder='Search'></input>
  				<i class="fa-solid fa-magnifying-glass search-icon"></i>
			</div>

			{/* <input className='NV-Search-Input' type='text' placeholder='Search'></input> */}
			<div className='NV-Right-Section'>
				{isLoaded && ( <ProfileButton user={sessionUser} /> )}
			</div>

		</div>
		
		</div>		           
		</>
	);
}

export default Navigation;