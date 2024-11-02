import React from 'react';
import Search from './Search';
import ButtonLogo from './ButtonLogo'
import MenuHeader from './MenuHeader'

const Header = ({handleButtonLogoClick, setMenuSelect}) => {

    return(
        <table class='header-table'>
            <td class='header-table-logo'><ButtonLogo handleClick={handleButtonLogoClick}/></td>
            <td class='header-table-search'><Search/></td>
            <td class='header-table-menu'><MenuHeader setName={setMenuSelect}/></td>
        </table>
    )
}

export default Header;