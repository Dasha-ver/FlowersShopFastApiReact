import roses_pic from '../pictures/roses-pic.jpg'
import bouquets_pic from '../pictures/bouquets-pic.png'
import flowers_box_pic from '../pictures/flowers-box-pic.png'
import flowers_in_basket_pic from '../pictures/flowers-in-basket-pic.jpg'
import toy_pic from '../pictures/toy-pic.jpg'
import balloon_pic from '../pictures/balloon-pic.png'
import gift_pic from '../pictures/gift-pic.jpg'
import card_pic from '../pictures/card-pic.jpg'
import celebrate_pic from '../pictures/celebrate-pic.jpg'
import to_whom_pic from '../pictures/to-whom-pic.jpg'
import by_the_piece_pic from '../pictures/by-the-piece-pic.jpg'


const CategoriesAndButtonsLine = () => {

    return (
        <table class='categories-buttons-line-table'>

                <td class='categories-buttons-line-table-td'>
                    <button class='categories-button'>
                        <img className="categories-buttons-pic" src={roses_pic} alt="roses_pic"/>
                            <div class='categories-title-div'>Розы</div>
                    </button>
                </td>
                <td class='categories-buttons-line-table-td'>
                    <button class='categories-button'>
                        <img className="categories-buttons-pic" src={bouquets_pic} alt="bouquets_pic"/>
                            <div class='categories-title-div'>Букеты</div>
                    </button>
                </td>
                <td class='categories-buttons-line-table-td'>
                    <button class='categories-button'>
                        <img className="categories-buttons-pic" src={flowers_box_pic} alt="flowers_box_pic"/>
                            <div class='categories-title-div'>Коробки</div>
                    </button>
                </td>
                <td class='categories-buttons-line-table-td'>
                    <button class='categories-button'>
                        <img className="categories-buttons-pic" src={flowers_in_basket_pic} alt="flowers_in_basket_pic"/>
                            <div class='categories-title-div'>Корзины</div>
                    </button>
                </td>
                <td class='categories-buttons-line-table-td'>
                    <button class='categories-button'>
                        <img className="categories-buttons-pic" src={toy_pic} alt="toy_pic"/>
                            <div class='categories-title-div'>Игрушки</div>
                    </button>
                </td>
                <td class='categories-buttons-line-table-td'>
                    <button class='categories-button'>
                        <img className="categories-buttons-pic" src={balloon_pic} alt="balloon_pic"/>
                            <div class='categories-title-div'>Шары</div>
                    </button>
                </td>
                <td class='categories-buttons-line-table-td'>
                    <button class='categories-button'>
                        <img className="categories-buttons-pic" src={gift_pic} alt="gift_pic"/>
                            <div class='categories-title-div'>Подарки</div>
                    </button>
                </td>
                <td class='categories-buttons-line-table-td'>
                    <button class='categories-button'>
                        <img className="categories-buttons-pic" src={card_pic} alt="card_pic"/>
                            <div class='categories-title-div'>Открытки</div>
                    </button>
                </td>
                <td class='categories-buttons-line-table-td'>
                    <button class='categories-button'>
                        <img className="categories-buttons-pic" src={celebrate_pic} alt="celebrate_pic"/>
                            <div class='categories-title-div'>Повод</div>
                    </button>
                </td>
                <td class='categories-buttons-line-table-td'>
                    <button class='categories-button'>
                        <img className="categories-buttons-pic" src={to_whom_pic} alt="to_whom_pic"/>
                            <div class='categories-title-div'>Кому</div>
                    </button>
                </td>
                <td class='categories-buttons-line-table-td'>
                    <button class='categories-button'>
                        <img className="categories-buttons-pic" src={by_the_piece_pic} alt="by_the_piece"/>
                            <div class='categories-title-div'>Поштучно</div>
                    </button>
                </td>

        </table>
        )
    }


export default CategoriesAndButtonsLine;