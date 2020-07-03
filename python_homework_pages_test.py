"""
Тест.

Тест, открывающий ya.ru, ищущий поисковую строку, затем вводим слово 'python'.
Если найдена поисковая строка, то происходит raise исключения.
"""
from selenium.webdriver.common.keys import Keys
from pages.python_homework_pages import YaPage


def test_page():
    """Начало теста."""
    ya_page = YaPage()
    ya_page.open_page()
    search_elem = ya_page.search_input()
    ya_page.expecting_condition()
    search_elem.send_keys('python')
    search_elem.send_keys(Keys.ENTER)
    assert 'По вашему запросу ничего не нашлось' not in ya_page.get_page_source()
    ya_page.quit_driver()


test_page()
