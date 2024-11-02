
const MenuHeader = (menu) => {

    return (
        <div class='dropdown'>
            <button class="menu-button">Меню</button>
                <div class="dropdown-content-menu">
                    <button onClick={() => menu.setName('payment')}>ОПЛАТА</button>
                    <button onClick={() => menu.setName('delivery')}>ДОСТАВКА</button>
                    <button>КОНТАКТЫ</button>
                    <button>БЛОГ</button>
                    <button>ОТЗЫВЫ</button>
                </div>
        </div>

)
}

export default MenuHeader;