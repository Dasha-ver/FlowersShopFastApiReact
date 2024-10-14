import {useLocation} from 'react-router-dom';
import React, {useState, useEffect} from 'react';
import ItemsTable from './ItemsTable'
import Header from './Header'
import InformationAndBasketLine from './InformationAndBasketLine'
import CategoriesButtonsLine from './CategoriesButtonsLine'
import HrLine from './HrLine'
import axios from "axios";

const SelectedCategoryPage = () => {

    const location = useLocation()
    const [category, setCategory] = useState(location.state.category)
    const [showMore, setShowMore] = useState(10)
    const [selectedItems, setSelectedItems] = useState([])

    async function getSelectedItems(selected, showMore) {
        const response = await axios.get('http://127.0.0.1:8000/api/'+selected+'/'+showMore)
        setSelectedItems(response.data)
    }

    useEffect(() => {
        setShowMore(20)
        getSelectedItems(category, 10)
        }, [category])

    const handleClick= () =>{
        setShowMore(showMore+10)
        getSelectedItems(category, showMore)
    }

    return(
        <div>
         <Header/>
            <InformationAndBasketLine/>
            <CategoriesButtonsLine setName={setCategory}/>
            <HrLine/>
            <ItemsTable handleClick={handleClick} items={selectedItems} />
         </div>

        )
}

export default SelectedCategoryPage;
