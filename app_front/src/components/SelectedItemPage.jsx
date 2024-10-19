import ItemCard from "./ItemCard";
import React, {useState, useEffect} from 'react';
import axios from "axios";
import Header from './Header'
import InformationAndBasketLine from './InformationAndBasketLine'
import CategoriesButtonsLine from './CategoriesButtonsLine'
import HrLine from './HrLine'
import {useNavigate} from 'react-router-dom';

const SelectedItemPage = () => {

    const navigate = useNavigate()
    const [items, setItems] = useState([])

    async function getSelectedItem() {
        const response = await axios.get('http://127.0.0.1:8000/api/balloon/4')
        setItems(response.data)
    }

    useEffect(() => {
        getSelectedItem()
        },[])

    const handleButtonLogoClick = () =>{
        navigate("/GeneralPage")
        }

    return(
        <div>

            <Header handleButtonLogoClick={handleButtonLogoClick}/>
            <InformationAndBasketLine/>
            <CategoriesButtonsLine/>
            <HrLine/>
            <div>
                {items.map(item => <ItemCard itemCard={item} key={item.id}/>)}
            </div>
        </div>

    )
}

export default SelectedItemPage;
