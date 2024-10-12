import datetime


class Base:
    """ Базовый класс, содержащий универсальные методы """

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        """Method get current url"""
        get_url = self.driver.current_url
        print("Current url: " + get_url)

    def assert_word(self, word, result):
        """Method assert word"""
        value_word = word.text
        assert value_word == result
        print("Good value word")

    def assert_url(self, result):
        """Проверка корректности URL"""
        get_url = self.driver.current_url
        print(get_url)
        assert result == get_url
        print("Корректная URL")

    def get_screenshot(self):
        """Создание скриншота"""
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = "screenshot " + now_date + ".png"
        # Относительный путь
        self.driver.save_screenshot(f"screen/{name_screenshot}")
        print("Скриншот выполнен")
