"""В это классе, мы объявили константу, которая явно указывает пои поисковую строку на ya.ru."""
from selenium.webdriver.common.by import By


class YaPageLocator:
    """Класс, содержащий константу. Константа содержит в себе локатор указывающий по поисковую строку."""

    INPUT_SEARCH_FIELD = (By.ID, 'text')
