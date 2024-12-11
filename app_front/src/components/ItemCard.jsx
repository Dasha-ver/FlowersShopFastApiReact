import React from "react";
import IncrementDecrementBtn from './IncrementDecrementBtn'
import InBasketBtn from './InBasketBtn'
import BuyWithOneClickBtn from './BuyWithOneClickBtn'
import card_pic from '../pictures/card-pic.jpg'
import balloon_pic from '../pictures/balloon-pic.png'
import sale_pic from '../pictures/sale-pic.png'
import delivery_pic from '../pictures/delivery-pic.jpg'
import paid_pic from '../pictures/paid-pic.png'
import Resource from "../services/resource.service";
import AuthService from "../services/auth.service";
import {useState, useEffect} from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";


const ItemCard = (props) => {

  const navigate = useNavigate();

  const [user, setUser] = useState('');
  const [category, setCategory] = useState(props.choseCategory)
  const [itemId, setItemId] = useState(props.itemCard.id)

  useEffect(() => {
    Resource.getCurrentUser().then(
      (response) => {
        setUser(response.data.id.toString());
      },
      (error) => {
        console.log("User page", error.response);
        // Invalid token
        if (error.response && error.response.status === 403) {
          AuthService.logout();
          navigate("/login");
          window.location.reload();
        }
      }
    );
  }, []);

const handleInBasket = () => {
    const data = {
      user_id: user,
      table_name: category,
      product_id: itemId
    };
      axios.post('http://127.0.0.1:8000/api/basket', data).then((response) => {
        console.log(response.status, response.data.token);
      });
  }

    return(
        <div class='item-card-div'>
            <table class='item-card-table'>
                <td class='item-card-img-td'>
                    <img class="item-card-img" src={props.itemCard.link} alt="No image"/>
                </td>
                <td class='item-card-desc-td'>
                    <tr class='item-card-title'>{props.itemCard.title}</tr>
                    <tr class='item-card-description'>{props.itemCard.description}</tr>
                    <hr class="hr-line-for-item-card"></hr>
                    <tr class='item-card-desc-tr'>
                        <td class='item-card-price'>{props.itemCard.price} BYN </td>
                        <td><IncrementDecrementBtn/></td>
                        <td><InBasketBtn handleInBasket={handleInBasket}/></td>
                        <td><BuyWithOneClickBtn/></td>
                    </tr>
                    <hr class="hr-line-for-item-card"></hr>
                    <tr>
                        <td>
                            <button class='item-card-add-card-balloon'>
                                <img class="item-card-pic" src={card_pic} alt="card_pic"/>
                                    Добавить открытку
                                        </button>
                                            </td>
                        <td>
                            <button class='item-card-add-card-balloon'>
                                <img class="item-card-pic" src={balloon_pic} alt="card_pic"/>
                                    Добавить шарик
                                        </button>
                                            </td>
                        </tr>
                        <tr class='item-card-condition'>
                            <td class='item-card-condition-td'>
                                <table>
                                    <tr class='item-card-condition-tr'>
                                        <img class="item-card-pic" src={sale_pic} alt="card_pic"/>
                                            % скидка
                                            </tr>
                                            <tr class='item-card-condition-desc-tr'>
                                                На цветы и букеты при самовывозе
                                                </tr>
                                                    </table>
                                                        </td>
                            <td class='item-card-condition-td'>
                                 <table>
                                    <tr class='item-card-condition-tr'>
                                        <img class="item-card-pic" src={delivery_pic} alt="card_pic"/>
                                            Условия доставки
                                            </tr>
                                                <tr class='item-card-condition-desc-tr'>
                                                    Курьером на дом или офис - 10 BYN в пределах МКАД. Бесплатно от 100 BYN
                                                        </tr>
                                                            </table>
                                                                </td>
                            <td class='item-card-condition-td'>
                                <table>
                                    <tr class='item-card-condition-tr'>
                                        <img class="item-card-pic" src={paid_pic} alt="card_pic"/>
                                            Способы оплаты
                                            </tr>
                                                <tr class='item-card-condition-desc-tr-paid'>
                                                    <ul>
                                                    <li>Безналичный расчет на сайте</li>
                                                    <li>Наличными курьеру</li>
                                                    <li>Картой курьеру</li>
                                                    </ul>
                                                        </tr>
                                                            </table>
                                                                </td>

                                </tr>
                    </td>

                </table>
        </div>

    )
}

export default ItemCard;