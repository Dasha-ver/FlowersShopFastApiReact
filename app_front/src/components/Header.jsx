import React from 'react';
import Search from './Search';
import ButtonLogo from './ButtonLogo'
import MenuHeader from './MenuHeader'
import {useState} from 'react';
import {useNavigate} from 'react-router-dom';

const Header = ({handleButtonLogoClick, handlePayment, handleDelivery, handleContacts}) => {

    return(
        <table class='header-table'>
            <td class='header-table-logo'><ButtonLogo handleClick={handleButtonLogoClick}/></td>
            <td class='header-table-search'><Search/></td>
            <td class='header-table-menu'><MenuHeader handlePayment={handlePayment} handleDelivery={handleDelivery}
                                                      handleContacts={handleContacts}/></td>
        </table>
    )
}

export default Header;