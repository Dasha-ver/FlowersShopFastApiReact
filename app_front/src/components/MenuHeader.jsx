
const MenuHeader = ({handlePayment, handleDelivery, handleContacts}) => {

    return (
        <div class='dropdown'>
            <button class="menu-button">Меню</button>
                <div class="dropdown-content-menu">
                    <button onClick={handlePayment}>ОПЛАТА</button>
                    <button onClick={handleDelivery}>ДОСТАВКА</button>
                    <button onClick={handleContacts}>КОНТАКТЫ</button>
                </div>
        </div>

)
}

export default MenuHeader;