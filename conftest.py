import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="Choose language: en, es, fr, etc.")

@pytest.fixture(scope="function")
def browser(request):
    # Получаем параметр языка из командной строки
    user_language = request.config.getoption("language")
    
    # Настройка опций для браузера Chrome
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    
    # Инициализация браузера
    browser = webdriver.Chrome(options=options)
    
    yield browser
    
    # Закрытие браузера после теста
    browser.quit()