import Header from './Header'
import InformationAndBasketLine from './InformationAndBasketLine'
import CategoriesButtonsLine from './CategoriesButtonsLine'
import HrLine from './HrLine'
import {useLocation, useNavigate} from 'react-router-dom';
import React, {useState} from 'react';
import Footer from './Footer'
import DescriptionForPayment from './DescriptionForPayment'
import DescriptionForDelivery from './DescriptionForDelivery'
import DescriptionForContacts from './DescriptionForContacts'

const SelectedMenuHeaderPage = () => {

    const location = useLocation()
    const navigate =useNavigate()
    const [category, setCategory] = useState('')
    const [menuSelect, setMenuSelect] = useState(location.state.select)

    if (category !== "" ){
        navigate("/kvetki.bel/category",{state:{category:category}})
    }

    const handleButtonLogoClick = () =>{
        navigate("/kvetki.bel")
        }

    const handlePayment = () =>{
        setMenuSelect('payment')
        }

    const handleDelivery = () =>{
        setMenuSelect('delivery')
        }

    const handleContacts = () =>{
        setMenuSelect('contacts')
        }

    return(
         <div>
            <Header handleButtonLogoClick={handleButtonLogoClick} handlePayment={handlePayment} handleDelivery={handleDelivery}
                    handleContacts={handleContacts}/>
            <InformationAndBasketLine/>
            <CategoriesButtonsLine setName={setCategory}/>
            <HrLine/>
                {(menuSelect === 'payment') ? <DescriptionForPayment/> :
                    (menuSelect === 'delivery') ? <DescriptionForDelivery/> :
                                                    <DescriptionForContacts/>
                    }

            <Footer/>
        </div>
        )
    }

export default SelectedMenuHeaderPage;