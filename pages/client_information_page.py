import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from base.base_class import Base
from faker import Faker


class Client_Information_Page(Base):
    """ Класс содержащий локаторы и методы для страницы информации о клиенте"""

    # Locators
    first_and_last_name = "//input[@name='Name']"
    email = "//input[@name='Email']"
    telephone = "//input[@name='tildaspec-phone-part[]']"
    telegram_login = "//input[@id='input_1700284684962']"
    whatsapp_radio_button = "//span[contains(text(), 'WhatsApp')]"
    promokod = '//input[@class="t-input t-inputpromocode js-tilda-rule"]'
    activate_promokod_button = '//div[@class="t-inputpromocode__btn t-btn t-btn_md"]'

    delivery_radio_button = "//span[contains(text(), 'Доставка СДЭК (до постамата)')]"
    place_select = '//input[@name="tildadelivery-pickup-name"]'

    full_name = "//input[@name='tildadelivery-userinitials']"
    comment_field = "//input[@name='tildadelivery-comment']"

    value_product = '(//div[@class="t706__product-title t-descr t-descr_sm"])[1]'
    price_product = '//span[@class="t706__cartwin-prodamount"]'

    # Getters

    def get_first_and_last_name(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.first_and_last_name)))

    def get_email(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_telephone(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.telephone)))

    def get_telegram_login(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.telegram_login)))

    def get_whatsapp_radio_button(self):
        return WebDriverWait(self.driver, 7).until(EC.element_to_be_clickable((By.XPATH, self.whatsapp_radio_button)))

    def get_promokod(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.promokod)))

    def get_activate_promokod_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.activate_promokod_button)))

    def get_delivery_radio_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.delivery_radio_button)))

    def get_place_select(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.place_select)))

    def get_full_name(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.full_name)))

    def get_comment_field(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.comment_field)))

    def get_value_product(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.value_product)))

    def get_price_product(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.price_product)))

    # Actions

    def input_first_and_last_name(self, first_and_last_name):
        self.get_first_and_last_name().send_keys(first_and_last_name)
        print("Input first name")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input email")

    def input_telephone(self, telephone):
        self.get_telephone().send_keys(telephone)
        print("Input telephone")

    def input_telegram_login(self, telegram_login):
        self.get_telegram_login().send_keys(telegram_login)
        print("Input telegram_login")

    def click_whatsapp_radio_button(self):
        self.get_whatsapp_radio_button().click()
        print('Click whatsapp radio button')

    def input_promokod(self, promokod):
        self.get_promokod().send_keys(promokod)
        print("Input full_name")

    def click_activate_promokod_button(self):
        self.get_activate_promokod_button().click()
        print('Click activate promokod button')

    def click_delivery_radio_button(self):
        self.get_delivery_radio_button().click()
        print('Click delivery radio button')

    def click_place_select(self):
        self.get_place_select().click()
        self.get_place_select().send_keys('MSK1610, Москва, ул. Большая Грузинская')
        self.get_place_select().send_keys(Keys. TAB)
        print('Click and select place')

    def input_full_name(self, full_name):
        self.get_full_name().send_keys(full_name)
        print("Input full_name")

    def input_comment_field(self, comment):
        self.get_comment_field().send_keys(comment)
        print("Input full_name")

    # Methods

    def input_information(self):
        """ Ввод информации о пользователе"""

        self.get_current_url()
        faker = Faker("ru_RU")      # Добавляем русский язык для генерации данных

        fake_name = faker.name_male()    # получение случайного мужского имени

        self.input_first_and_last_name(fake_name)

        fake_email = faker.email()       # получение случайного email
        self.input_email(fake_email)

        self.input_telephone('9991112233')

        self.input_telegram_login('@test')
        self.click_whatsapp_radio_button()

        self.input_promokod('TEST')
        self.click_activate_promokod_button()
        WebDriverWait(self.driver, 4).until(EC.alert_is_present(), 'Timed out waiting for PA creation ')
        alert = self.driver.switch_to.alert
        alert.accept()

        time.sleep(2)
        self.click_delivery_radio_button()
        time.sleep(1.5)
        self.click_place_select()
        self.input_full_name(fake_name)
        self.input_comment_field("Test-OK")
# кнопка "купить" не доступна при автоматизированном тесте сайта, поэтому без неё

    def text_value_and_price_product(self):
        """Получение имени и цены товара"""

        value = self.get_value_product().text.split("\n")[0]
        price = self.get_price_product().text
        print(value, price)
        return value, price
