import location_pic from '../pictures/location-pic.webp'
import google_map_pic from '../pictures/google-map-pic.webp'

const ShopsLocation = () => {

    return (
        <div class='dropdown'>
            <button class="shops-location-button">Адреса наших магазинов<img className="location-pic" src={location_pic} alt="location-pic"/></button>
                <div class="dropdown-content-shops-location">
                    <tr><button> КАРАСТОЯНОВОЙ, 33 <img className="google-map-pic" src={google_map_pic} alt="google-map-pic"/></button></tr>
                    <tr><button>МАЗУРОВА, 4 <img className="google-map-pic" src={google_map_pic} alt="google-map-pic"/></button></tr>
                </div>
        </div>

)
}

export default ShopsLocation;

