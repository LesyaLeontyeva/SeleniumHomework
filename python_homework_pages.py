"""Функции для работы со страницей ya.ru."""
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from python_locators.python_homework_locators import YaPageLocator
from webdriver_manager.chrome import ChromeDriverManager

YA_URL = 'https://ya.ru/'


class MyError(Exception):
    """Самописное исключение для работы со временем ожидания страницы."""

    def __init__(self, message):
        """Вызывет магический метод __init__."""
        self.message = message


class YaPage:
    """Класс для работы с главной страницей ya.ru."""

    driver = webdriver.Chrome(ChromeDriverManager().install())

    def search_input(self):
        """Функция, для работы с нахождением поиискойо строки на ya.ru."""
        self.driver.get(YA_URL)
        elem = YaPage.driver.find_element(*YaPageLocator.INPUT_SEARCH_FIELD)
        return elem

    def expecting_condition(self, locator='text', time_for_wait=5):
        """Функция для работы с ожиданием времени нахождения поисковой строки."""
        try:
            WebDriverWait(YaPage.driver, time_for_wait).until(EC.presence_of_element_located((By.ID, locator)))
        except TimeoutException:
            raise MyError('Время ожидания страницы истекло')

    def open_page(self):
        """Фукнция для открытия страницы, URL страница нах-ся в константе YA_URL."""
        self.driver.get(YA_URL)

    def quit_driver(self):
        """Фукнция для закрытия браузера после окончания теста."""
        self.driver.quit()

    def get_page_source(self):
        """Функция получения всей страницы целиком."""
        return self.driver.page_source
