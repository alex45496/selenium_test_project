import pytest

from pages.client_information_page import Client_Information_Page
from pages.main_page import Main_Page


testdata = [
            (2, 1, 'Кружки ☕'),
            (4, 2, 'Стикеры 3D'),
            (9, 3, 'Свитшоты 🧥')
            ]


@pytest.mark.parametrize("n_filter, n_elem, expected", testdata)
def test_buy_product(n_filter, n_elem, expected, set_up):
    """Тест по покупке товара включает:
    - 1. выбор фильтра для товара
    - 2. Покупка товара
    - 3. Проверка товара по фильтру
    - 4. Проверка цены и названия товара
    - 5. Заполнение информации о пользователе"""

    driver = set_up   # смотреть conftest

    mp = Main_Page(driver, n_filter, n_elem, expected)
    mp.select_filter()

    mp.select_products()
    main_info_product = mp.text_value_and_price_product()

    clp = Client_Information_Page(driver)
    client_cart_info_product = clp.text_value_and_price_product()

    assert main_info_product == client_cart_info_product
    print("Информация о товаре на основной странице совпадает с информацией в корзине")

    clp.input_information()
