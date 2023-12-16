import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import hypeLogo from '../../images/hypeicon.png'
import './Navigation.css';

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);

	return (
		<>
		<div className='NV-Main-Div'>

		<div className='NV-Left-Div'>	
		<div className='NV-Menu-Left-Options'>
			<img src={hypeLogo} alt='hype logo' className='NV-Logo'></img>		
		</div>

		<div className='NV-Menu-Right-Options'>
			<div className='NV-Menu-Options'>
				Home
			</div>
			<div className='NV-Menu-Options'>
				Browse
			</div>
			<div className='NV-Menu-Options'>
				Upload
			</div>
		</div>
		</div>

		<div className='NV-Right-Div'>
			<div className='NV-Right-Section'>
				{isLoaded && ( <ProfileButton user={sessionUser} /> )}
			</div>

		</div>
		
		</div>		           
		</>
	);
}

export default Navigation;