from selenium.webdriver.common.by import By
import time

def test_guest_should_see_add_to_basket_button(browser):
    # Переход на страницу товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Ждем 30 секунд для визуальной проверки
    time.sleep(30)
    
    # Поиск кнопки добавления в корзину
    button = browser.find_element("css selector", ".btn-add-to-basket")
    
    # Проверка, что кнопка присутствует на странице
    assert button is not None, "Кнопка добавления в корзину не найдена"