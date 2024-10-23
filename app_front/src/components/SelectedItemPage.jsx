import ItemCard from "./ItemCard";
import React, {useState, useEffect} from 'react';
import axios from "axios";
import Header from './Header'
import InformationAndBasketLine from './InformationAndBasketLine'
import CategoriesButtonsLine from './CategoriesButtonsLine'
import HrLine from './HrLine'
import {useNavigate, useLocation} from 'react-router-dom';

const SelectedItemPage = () => {

    const navigate = useNavigate()
    const location = useLocation()
    const [items, setItems] = useState([])
    const [category, setCategory] = useState('')

    if (category !== ''){
         navigate("/kvetki.bel/category", {state:{category:category}})
        }

    async function getSelectedItem() {
        const response = await axios.get('http://127.0.0.1:8000/api/'+location.state.category+'/'+location.state.id)
        setItems(response.data)
    }

    useEffect(() => {
        getSelectedItem()
        },[])

    const handleButtonLogoClick = () =>{
        navigate("/kvetki.bel")
        }

    return(
        <div>
            <Header handleButtonLogoClick={handleButtonLogoClick}/>
            <InformationAndBasketLine/>
            <CategoriesButtonsLine setName={setCategory}/>
            <HrLine/>
            {category}
            <div>
                {items.map(item => <ItemCard itemCard={item} key={item.id}/>)}
            </div>
        </div>

    )
}

export default SelectedItemPage;
