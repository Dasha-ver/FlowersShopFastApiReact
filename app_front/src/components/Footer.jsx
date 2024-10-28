import loc_pic from '../pictures/loc-pic.png'
import phone_pic from '../pictures/phone-pic.png'
import mail_pic from '../pictures/mail-pic.png'
import watch_pic from '../pictures/watch-pic.png'
import insta_pic from '../pictures/insta-pic.png'
import facebook_pic from '../pictures/facebook-pic.png'
import youtube_pic from '../pictures/youtube-pic.png'
import belkart_pic from '../pictures/belkart-pic.png'
import mastercard_pic from '../pictures/mastercard-pic.png'
import visa_pic from '../pictures/visa-pic.png'


const Footer = () => {

    return(
        <div>
            <table class='footer-table'>
            <tr>
                <td class= 'footer-td'>
                    <tr class= 'footer'>
                        Режим работы и адрес
                        </tr>
                        <hr class="hr-line-for-item-card"></hr>
                            <form action="https://www.google.by/maps/place/%D1%83%D0%BB.+%D0%9B%D0%B8%D0%BB%D0%B8%D0%B8+%D0%9A%D0%B0%D1%80%D0%B0%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%BE%D0%B2%D0%BE%D0%B9+33,+%D0%9C%D0%B8%D0%BD%D1%81%D0%BA,+%D0%9C%D0%B8%D0%BD%D1%81%D0%BA%D0%B0%D1%8F+%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C/@53.9376668,27.562927,17z/data=!3m1!4b1!4m6!3m5!1s0x46dbcf7c9932f95f:0x4800080b2fb16373!8m2!3d53.9376668!4d27.5655019!16s%2Fg%2F11dzn5md4x?entry=ttu&g_ep=EgoyMDI0MTAwOS4wIKXMDSoASAFQAw%3D%3D" target="_blank">
                                <tr class= 'footer-tr'><button class='footer-btn'> <img className="loc-pic" src={loc_pic} alt="loc-pic"/> КАРАСТОЯНОВОЙ, 33 </button></tr>
                            </form>
                            <form action="https://www.google.by/maps/place/%D1%83%D0%BB.+%D0%9C%D0%B0%D0%B7%D1%83%D1%80%D0%BE%D0%B2%D0%B0+4,+%D0%9C%D0%B8%D0%BD%D1%81%D0%BA,+%D0%9C%D0%B8%D0%BD%D1%81%D0%BA%D0%B0%D1%8F+%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C+220140/@53.8962828,27.4285663,17z/data=!3m1!4b1!4m6!3m5!1s0x46dbdad8b4f4114b:0x9c60e1f6aa8f9e2f!8m2!3d53.8962828!4d27.4311412!16s%2Fg%2F11cp8sfz47?entry=ttu&g_ep=EgoyMDI0MTAwOS4wIKXMDSoASAFQAw%3D%3D" target="_blank">
                                <tr class= 'footer-tr'><button class='footer-btn'> <img className="loc-pic" src={loc_pic} alt="loc-pic"/> МАЗУРОВА, 4 </button></tr>
                            </form>
                        <tr class= 'footer-tr'>
                            <img className="footer-pic" src={phone_pic} alt="footer-pic"/>+375 (29) 711-18-33
                        </tr>
                        <tr class= 'footer-tr'>
                            <img className="footer-pic" src={phone_pic} alt="footer-pic"/>+375 (44) 571-41-41
                        </tr>
                        <tr class= 'footer-tr'>
                            <img className="footer-pic" src={mail_pic} alt="footer-pic"/>kvetki.bel@mail.ru
                        </tr>
                        <tr class= 'footer-tr'>
                            <img className="footer-pic" src={watch_pic} alt="footer-pic"/>Пн - Вс - с 9:00 по 22:00
                        </tr>
                    </td>

                        <td class= 'footer-td-right'>
                            <tr class= 'footer'>
                                Подписывайтесь на нас
                        </tr>
                         <hr class="hr-line-for-item-card"></hr>
                         <tr class= 'footer'>
                                <button class='footer-media-btn'><img className="footer-pic" src={insta_pic} alt="footer-pic"/></button>
                                <button class='footer-media-btn'><img className="footer-pic" src={facebook_pic} alt="footer-pic"/></button>
                                <button class='footer-media-btn'><img className="footer-pic" src={youtube_pic} alt="footer-pic"/></button>
                        </tr>
                            </td>
                </tr>
        </table>
        <table class='footer-table'>
            <tr class= 'footer'>
                <img className="footer-paid-system-belkart-pic" src={belkart_pic} alt="footer-pic"/>
                <img className="footer-paid-system-pic" src={mastercard_pic} alt="footer-pic"/>
                <img className="footer-paid-system-pic" src={visa_pic} alt="footer-pic"/>
                </tr>
        </table>
    </div>
        )
    }

export default Footer;