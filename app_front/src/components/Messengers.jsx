import insta_pic from '../pictures/insta-pic.png'
import telega_pic from '../pictures/telega-pic.png'
import whatsapp_pic from '../pictures/whatsapp-pic.png'



const Messengers = () => {

    return (
        <div>
            <table >
                <td><button class='messengers-table-button'><img className="messengers-pic" src={insta_pic} alt="insta-pic"/></button></td>
                 <td><button class='messengers-table-button'><img className="messengers-pic" src={telega_pic} alt="telega-pic"/></button></td>
                  <td><button class='messengers-table-button'><img className="messengers-pic" src={whatsapp_pic} alt="whatsapp-pic"/></button></td>
                </table>

            </div>
        )
    }


export default Messengers;