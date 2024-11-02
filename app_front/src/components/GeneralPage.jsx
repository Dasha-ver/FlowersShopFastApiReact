import Header from './Header'
import InformationAndBasketLine from './InformationAndBasketLine'
import CategoriesButtonsLine from './CategoriesButtonsLine'
import HrLine from './HrLine'
import FlowersDeliveryTitle from './FlowersDeliveryTitle'
import GeneralPageBannerSale from './GeneralPageBannerSale'
import {useNavigate} from 'react-router-dom';
import React, {useState} from 'react';
import DescriptionForGeneralPage from './DescriptionForGeneralPage'
import Footer from './Footer'

const GeneralPage = () => {

    const navigate = useNavigate()
    const [category, setCategory] = useState('')

    navigate("/kvetki.bel/category",{state:{category:category}})

    const setMenuSelect = () => {
        navigate("/kvetki.bel/description")
        }

    return(
        <div>
            <Header setMenuSelect={setMenuSelect}/>
            <InformationAndBasketLine />
            <CategoriesButtonsLine setName={setCategory}/>
            <HrLine/>
            <FlowersDeliveryTitle/>
            <GeneralPageBannerSale/>
            <DescriptionForGeneralPage/>
            <Footer/>
        </div>
    )
}

export default GeneralPage;