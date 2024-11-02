import {useLocation, useNavigate} from 'react-router-dom';
import React, {useState, useEffect} from 'react';
import ItemsTable from './ItemsTable'
import RangeSlider from './RangeSlider'
import Header from './Header'
import InformationAndBasketLine from './InformationAndBasketLine'
import CategoriesButtonsLine from './CategoriesButtonsLine'
import HrLine from './HrLine'
import axios from "axios";
import DescriptionForBouquets from './DescriptionForBouquets'
import DescriptionForBouquetsOfRoses from './DescriptionForBouquetsOfRoses'
import DescriptionForFlowersBoxes from './DescriptionForFlowersBoxes'
import DescriptionForBasket from './DescriptionForBasket'
import DescriptionForToys from './DescriptionForToys'
import DescriptionForBalloons from './DescriptionForBalloons'
import DescriptionForPresents from './DescriptionForPresents'
import DescriptionForCards from './DescriptionForCards'
import Description from './Description'
import Footer from './Footer'

const SelectedCategoryPage = () => {
    const location = useLocation()
    const navigate = useNavigate()
    const [category, setCategory] = useState(location.state.category)
    const [showMore, setShowMore] = useState(10)
    const [selectedItems, setSelectedItems] = useState([])
    const [value, setValue] = useState({ min: 0, max: 1500 });

    async function getSelectedItems(selected, minPrice, maxPrice, showMore) {
        const response = await axios.get('http://127.0.0.1:8000/api/'+selected+'/'+minPrice+'/'+maxPrice+'/'+showMore)
        setSelectedItems(response.data)
    }

    useEffect(() => {
        setShowMore(20)
        getSelectedItems(category, value.min, value.max, 10)
        }, [category, value.min, value.max])

    const handleClick = () =>{
        setShowMore(showMore+10)
        getSelectedItems(category, value.min, value.max, showMore)
    }

    const handleButtonLogoClick = () =>{
        navigate("/kvetki.bel")
        }

    const setMenuSelect = () => {
        navigate("/kvetki.bel/description")
        }

    return(
        <div>
            <Header handleButtonLogoClick={handleButtonLogoClick} setMenuSelect={setMenuSelect}/>
            <InformationAndBasketLine/>
            <CategoriesButtonsLine setName={setCategory}/>
            <HrLine/>
            <table class='range-slider-table'>
                <td class='range-slider-min-value-td'><td>{value.min} BYN</td><td class='symbol'>&gt;</td></td>
                <td class='range-slider-td'>
                    <RangeSlider min={0} max={1500} step={5} value={value} onChange={setValue}/></td>
                 <td class='range-slider-max-value-td'><td class='symbol'>&lt;</td><td>{value.max} BYN</td></td>
             </table>
            <ItemsTable handleClick={handleClick} items={selectedItems} category={category}/>
                {(category === 'bouquets') ? <DescriptionForBouquets/> :
                    (category === 'flowers_boxes') ? <DescriptionForFlowersBoxes/> :
                        (category === 'bouquets_of_roses') ? <DescriptionForBouquetsOfRoses/> :
                            (category === 'flowers_baskets') ? <DescriptionForBasket/> :
                                (category === 'toys') ? <DescriptionForToys/> :
                                    (category === 'balloons') ? <DescriptionForBalloons/> :
                                        (category === 'presents') ? <DescriptionForPresents/> :
                                            (category === 'cards') ? <DescriptionForCards/> :
                                                <Description/>
                }
            <Footer/>
         </div>

        )
}

export default SelectedCategoryPage;
