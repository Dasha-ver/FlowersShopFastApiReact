import Header from './Header'
import InformationAndBasketLine from './InformationAndBasketLine'
import CategoriesButtonsLine from './CategoriesButtonsLine'
import HrLine from './HrLine'
import FlowersDeliveryTitle from './FlowersDeliveryTitle'
import GeneralPageBannerSale from './GeneralPageBannerSale'
import {useNavigate} from 'react-router-dom';
import React, {useState} from 'react';

const GeneralPage = () => {

    const navigate = useNavigate()
    const [category, setCategory] = useState('')

    navigate("/SelectedCategoryPage",{state:{category:category}})

    return(
        <div>
            <Header/>
            <InformationAndBasketLine />
            <CategoriesButtonsLine setName={setCategory}/>
            <HrLine/>
            <FlowersDeliveryTitle/>
            <GeneralPageBannerSale/>
        </div>

    )
}

export default GeneralPage;