import React from "react";

const ButtonLogo = ({handleClick}) => {

    return(
        <div>
            <button class='button-logo' onClick={handleClick}>
                <div class='flower-shop-logo'>Flower shop</div>
                <td class='shop-name-logo-kvetki'>KVETKI.</td>
                <td class='shop-name-logo-bel'>BEL</td>
            </button>
        </div>
)
}


export default ButtonLogo;


