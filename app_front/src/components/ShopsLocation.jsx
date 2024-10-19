import location_pic from '../pictures/location-pic.webp'
import google_map_pic from '../pictures/google-map-pic.webp'

const ShopsLocation = () => {

    return (
        <div class='dropdown'>
            <button class="shops-location-button">Адреса наших магазинов<img className="location-pic" src={location_pic} alt="location-pic"/></button>
                <div class="dropdown-content-shops-location">
                    <form action="https://www.google.by/maps/place/%D1%83%D0%BB.+%D0%9B%D0%B8%D0%BB%D0%B8%D0%B8+%D0%9A%D0%B0%D1%80%D0%B0%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%BE%D0%B2%D0%BE%D0%B9+33,+%D0%9C%D0%B8%D0%BD%D1%81%D0%BA,+%D0%9C%D0%B8%D0%BD%D1%81%D0%BA%D0%B0%D1%8F+%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C/@53.9376668,27.562927,17z/data=!3m1!4b1!4m6!3m5!1s0x46dbcf7c9932f95f:0x4800080b2fb16373!8m2!3d53.9376668!4d27.5655019!16s%2Fg%2F11dzn5md4x?entry=ttu&g_ep=EgoyMDI0MTAwOS4wIKXMDSoASAFQAw%3D%3D" target="_blank">
                        <tr><button> КАРАСТОЯНОВОЙ, 33 <img className="google-map-pic" src={google_map_pic} alt="google-map-pic"/></button></tr>
                    </form>
                    <form action="https://www.google.by/maps/place/%D1%83%D0%BB.+%D0%9C%D0%B0%D0%B7%D1%83%D1%80%D0%BE%D0%B2%D0%B0+4,+%D0%9C%D0%B8%D0%BD%D1%81%D0%BA,+%D0%9C%D0%B8%D0%BD%D1%81%D0%BA%D0%B0%D1%8F+%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C+220140/@53.8962828,27.4285663,17z/data=!3m1!4b1!4m6!3m5!1s0x46dbdad8b4f4114b:0x9c60e1f6aa8f9e2f!8m2!3d53.8962828!4d27.4311412!16s%2Fg%2F11cp8sfz47?entry=ttu&g_ep=EgoyMDI0MTAwOS4wIKXMDSoASAFQAw%3D%3D" target="_blank">
                        <tr><button>МАЗУРОВА, 4 <img className="google-map-pic" src={google_map_pic} alt="google-map-pic"/></button></tr>
                    </form>
                </div>
        </div>

)
}

export default ShopsLocation;

