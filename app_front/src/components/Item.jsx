import React from "react";
import basket_pic from '../pictures/basket-pic.png'

const Item = (props) => {

    return(

         <tr>
             <td>
                    <table class='item-table'>
                        <tr>
                            <img class="item-img" src={props.item.link} alt="No image"/>
                        </tr>
                        <tr class='item-title'>
                            {props.item.title}
                        </tr>

                        <tr class='item-price-tr'>
                            <div>
                                <td class='item-price'>{props.item.price} BYN </td>
                                <td class='item-basket'><img className="basket-pic-item" src={basket_pic} alt="basket-pic"/></td>
                            </div>
                        </tr>

                        </table>
                </td>
        </tr>
    )
}

export default Item;