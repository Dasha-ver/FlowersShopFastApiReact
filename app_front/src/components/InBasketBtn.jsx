import in_basket_pic from '../pictures/in-basket-pic.png'

const InBasketBtn = ({handleInBasket}) => {


    return (

          <button class="in-basket-button" onClick={handleInBasket}><img className="in-basket-pic" src={in_basket_pic} alt="basket-pic"/>В корзину</button>

    )
}
export default InBasketBtn;
