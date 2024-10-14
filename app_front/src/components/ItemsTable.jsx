import Item from "./Item";
import React, {useState, useEffect} from 'react';
import axios from "axios";

const ItemsTable = ({items, handleClick}) => {

    return(
        <div>
            <table class="items-table">
                {items.map(item => <Item item={item} key={item.id}/>)}
            </table>
            <div class='btn-show-more-div'>
                <button class="btn-show-more" onClick= {handleClick}>Показать ещё 10 товаров</button>
            </div>
        </div>

    )
}

export default ItemsTable;
