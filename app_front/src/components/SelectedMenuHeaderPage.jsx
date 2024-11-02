import Header from './Header'
import InformationAndBasketLine from './InformationAndBasketLine'
import CategoriesButtonsLine from './CategoriesButtonsLine'
import HrLine from './HrLine'
import {useNavigate} from 'react-router-dom';
import React, {useState} from 'react';
import Footer from './Footer'
import DescriptionForPayment from './DescriptionForPayment'
import DescriptionForDelivery from './DescriptionForDelivery'

const SelectedMenuHeaderPage = () => {

    const navigate = useNavigate()
    const [category, setCategory] = useState('')
    const [menuSelect, setMenuSelect] = useState('')

    navigate("/kvetki.bel/category",{state:{category:category}})

    const handleButtonLogoClick = () =>{
        navigate("/kvetki.bel")
        }

    return(
         <div>
            <Header handleButtonLogoClick={handleButtonLogoClick} setMenuSelect={setMenuSelect}/>
            <InformationAndBasketLine/>
            <CategoriesButtonsLine setName={setCategory}/>
            <HrLine/>
            {menuSelect}
                {(menuSelect === 'delivery') ? <DescriptionForDelivery/> :
                    (menuSelect === 'delivery') ? <DescriptionForDelivery/> :
                                                    <DescriptionForPayment/>
                    }

        <Footer/>
        </div>
        )
    }

export default SelectedMenuHeaderPage;