import Header from './Header'
import InformationAndBasketLine from './InformationAndBasketLine'
import CategoriesButtonsLine from './CategoriesButtonsLine'
import HrLine from './HrLine'
import FlowersDeliveryTitle from './FlowersDeliveryTitle'
import GeneralPageBannerSale from './GeneralPageBannerSale'


const GeneralPage = () => {

    return(
        <div>
            <Header/>
            <InformationAndBasketLine/>
            <CategoriesButtonsLine/>
            <HrLine/>
            <FlowersDeliveryTitle/>
            <GeneralPageBannerSale/>
        </div>

    )
}

export default GeneralPage;