import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from base.base_class import Base


class Main_Page(Base):
    """ Класс содержащий локаторы и методы для основной страницы магазина"""

    def __init__(self, driver, n_filter, n_elem, expected):
        super().__init__(driver)
        self.driver = driver
        self.n_filter = n_filter    # номер фильтра на странице
        self.n_elem = n_elem        # номер товара на странице
        self.expected = expected    # переданный фильтр

    # Locators
    filter_item = '(//div[@class="js-store-parts-switcher t-store__parts-switch-btn t-name t-name_xs t-menu__link-item"])'  # фильтр для выбора товара

    select_product = "(//span[contains(text(), 'В корзину')])"               # добавить товар в корзину
    value_product = '(//div[@class="js-store-prod-name js-product-name t-store__card__title t-typography__title t-name t-name_xs"])'
    price_product = '(//div[@class="t-store__card__price t-store__card__price-item t-name t-name_xs"])'

    cart = "//div[@class='t706__carticon t706__carticon_sm t706__carticon_showed']"     # корзина
    buy_button = "//button[@class='t706__sidebar-continue t-btn']"                      # кнопка купить в корзине

    # Getters

    def get_filter_item(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, f"{self.filter_item}{[self.n_filter]}")))

    def get_select_product(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, f"{self.select_product}{[self.n_elem]}")))

    def get_value_product(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, f"{self.value_product}{[self.n_elem]}")))

    def get_price_product(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, f"{self.price_product}{[self.n_elem]}")))

    def get_cart(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_buy_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.buy_button)))

    # Actions

    def click_filter_item(self):
        filter_name = self.get_filter_item()
        filter_name.click()
        print(f"Выбран фильтр: {filter_name.text}")
        assert filter_name.text == self.expected
        print("Выбранный фильтр совпадает - ОК")

    def click_select_product(self):
        self.get_select_product().click()
        print("Click select product")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    def click_buy_button(self):
        self.get_buy_button().click()
        print("Click buy button")

    # Methods

    def select_filter(self):
        """Выбор фильтра товара"""

        self.get_current_url()
        self.click_filter_item()
        time.sleep(1)

    def select_products(self):
        """Выбор товара и переход в корзину"""

        self.get_current_url()
        self.click_select_product()
        self.click_cart()
        self.click_buy_button()

    def text_value_and_price_product(self):
        """Получение имени и цены товара"""
        value = self.get_value_product().text
        price = self.get_price_product().text
        print(value, price)
        return value, price
