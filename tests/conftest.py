import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def set_up():
    """Действия перед каждым тестом: настройка браузера"""

    print("\nЗапуск теста")

    options = webdriver.ChromeOptions()              # возможность добавлять дополнительные настройки для браузера
    options.add_experimental_option('detach', True)  # опция, которая не позволит нашему браузеру закрыться

    options.add_argument("--disable-notifications")
    # options.add_argument("--headless=old")         # Открытие браузера в headless режиме (без отображения браузера)
    # options.page_load_strategy = 'eager'           # для Chrome, чтобы не ждать загрузки страницы

    service = Service(executable_path="../chromedriver.exe")  # указываем путь до скаченного chromedriver (драйвер для Google Chrome)
    driver = webdriver.Chrome(service=service, options=options)  # экземляр класса для управления браузером

    url = 'https://shop.pygen.ru/'
    driver.get(url)
    driver.maximize_window()

    yield driver

    print("\nТест завершен!")
    driver.quit()
