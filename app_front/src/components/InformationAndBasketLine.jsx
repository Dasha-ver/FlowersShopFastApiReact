import ShopsLocation from './ShopsLocation';
import Messengers from './Messengers'
import Contacts from './Contacts'
import AuthTable from '../authComponents/AuthTable'


const InformationAndBasketLine = () => {

    return (
        <div class='information-basket-line-div'>
                <td class='info-basket-table-td-shops-location'><ShopsLocation/></td>
                 <td class='info-basket-table-td-messengers'><Messengers/></td>
                  <td class='info-basket-table-td-contacts'><Contacts/></td>
                   <td class='info-basket-table-td-auth-table'><AuthTable/></td>
            </div>
        )
    }


export default InformationAndBasketLine;