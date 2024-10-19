import Item from "./Item";
import React, {useState, useEffect} from 'react';
import axios from "axios";
import {useNavigate} from 'react-router-dom';


const ItemsTable = ({items, handleClick, category}) => {

    const navigate = useNavigate()

    return(
        <div>
            {category}
            <table class="items-table">
                {items.map(item => <button class='item-button' onClick={() => navigate("/SelectedItemPage")}>
                    <Item item={item} key={item.id}/></button>)}
            </table>
            <div class='btn-show-more-div'>
                <button class="btn-show-more" onClick= {handleClick}>Показать ещё 10 товаров</button>
            </div>
        </div>


    )
}

export default ItemsTable;
