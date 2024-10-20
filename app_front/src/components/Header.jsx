import React from 'react';
import {useNavigate} from 'react-router-dom';
import Search from './Search';
import ButtonLogo from './ButtonLogo'
import MenuHeader from './MenuHeader'

const Header = ({handleButtonLogoClick}) => {

    const navigate = useNavigate()

    return(
        <table class='header-table'>
            <td class='header-table-logo'><ButtonLogo handleClick={handleButtonLogoClick}/></td>
            <td class='header-table-search'><Search/></td>
            <td class='header-table-menu'><MenuHeader/></td>
        </table>
    )
}

export default Header;