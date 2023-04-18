from selenium.webdriver.common.by import By
import time
from pages.pages import AuthPage, RegPage, AuthOnlimePage, AuthStartPage, AuthSmarthomePage, AuthKeyPage
from pages.config import long_name_259, long_phone_259, long_password_259, phone, email, password, lc

# запуск тестов из консоли:
# pytest -v --driver Chrome --driver-path ./chromedriver.exe  tests/test_pages.py


def test_reg_page_boundary_values_names_passwords(selenium):
    """
    1. Продукт ЕЛК web. Регистрация. Позитивный (bug)
    """
    page = RegPage(selenium)
    page.enter_name("А-")
    page.enter_surname("Ф-")
    page.enter_email("abcd@mail.ru")
    page.enter_pass("yV6vdvMi")
    page.enter_pass_confirm("yV6vdvMi")
    page.btn_click()

    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'
    assert selenium.find_element(By.ID, "rt-code-0")


def test_reg_page_empty_values(selenium):
    """
    2. Продукт ЕЛК web. Регистрация. Негативный    
    """
    page = RegPage(selenium)
    time.sleep(5) #ждем реакции
    page.enter_name("")
    page.enter_surname("")
    page.enter_email("")
    page.enter_pass("")
    page.enter_pass_confirm("")
    page.btn.click()

    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'


def test_reg_page_boundary_values_names_30_and_not_confirm(selenium):
    """
    3. Продукт ЕЛК web. Регистрация. Негативный     
    """
    page = RegPage(selenium)
    page.enter_name("")
    page.enter_surname("Через-Забор-Ногу-Задирищенский")
    page.enter_email("Через-Забор-Ногу-Задирищенский")
    page.enter_pass("Ww123456")
    page.enter_pass_confirm("Ww12345")
    page.btn_click()

    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'


def test_reg_page_boundary_values_259(selenium):
    """
    4. Продукт ЕЛК web. Регистрация. Негативный     
    """
    page = RegPage(selenium)
    page.enter_name(long_name_259)
    page.enter_surname(long_name_259)
    page.enter_phone(long_phone_259)
    page.enter_pass(long_password_259)
    page.enter_pass_confirm(long_password_259)
    page.btn_click()

    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'


def test_auth_elk_page_phone(selenium):
    """
    5. Продукт ЕЛК web. Авторизация. Позитивный     
    """
    page = AuthPage(selenium)
    page.enter_phone(phone)
    page.enter_pass(password)
    page.btn_click()

    assert page.get_relative_link() == '/account_b2c/page'
    selenium.find_element(By.ID, "logout-btn").click()


def test_auth_elk_page_email(selenium):
    """
    6. Продукт ЕЛК web. Авторизация. Позитивный     
    """
    page = AuthPage(selenium)
    page.enter_email(email)
    page.enter_pass(password)
    page.btn_click()

    assert page.get_relative_link() == '/account_b2c/page'
    selenium.find_element(By.ID, "logout-btn").click()


def test_auth_elk_page_lc(selenium):
    """
    7. Продукт ЕЛК web. Авторизация. Позитивный     
    """
    page = AuthPage(selenium)
    page.enter_lc(lc)
    page.enter_pass(password)
    page.btn_click()

    assert page.get_relative_link() == '/account_b2c/page'
    selenium.find_element(By.ID, "logout-btn").click()


def test_auth_elk_page_phone_symbols(selenium):
    """
    8. Продукт ЕЛК web. Авторизация. Негативный    
    """
    page = AuthPage(selenium)
    page.enter_phone("абвгд")
    page.enter_pass(password)
    page.btn_click()

    assert page.get_relative_link() == '/account_b2c/page'

 
def test_auth_onlime_page_phone(selenium):
    """
    9. Продукт Онлайм web. Авторизация. Позитивный     
    """
    page = AuthOnlimePage(selenium)
    page.enter_email(phone)
    page.enter_pass(password)
    page.btn_click()

    assert page.get_relative_link() == '/account_b2c/page'
    selenium.find_element(By.ID, "logout-btn").click()

 
def test_auth_onlime_page_email(selenium):
    """
    10. Продукт Онлайм web. Авторизация. Позитивный     
    """
    page = AuthOnlimePage(selenium)
    page.enter_email(email)
    page.enter_pass(password)
    page.btn_click()

    assert page.get_relative_link() == '/account_b2c/page'
    selenium.find_element(By.ID, "logout-btn").click()

 
def test_auth_onlime_page_email_incorrect(selenium):
    """
    11. Продукт Онлайм web. Авторизация. Негативный     
    """
    page = AuthOnlimePage(selenium)
    page.enter_email("Albuquerque@gmail.com")
    page.enter_pass(password)
    page.btn_click()

    assert selenium.find_element(By.ID, "form-error-message")


def test_auth_start_page_phone(selenium):
    """
    12. Продукт Старт web. Авторизация. Позитивный  
    """
    page = AuthStartPage(selenium)
    page.enter_email(phone)
    page.enter_pass(password)
    page.btn_click()

    assert page.get_relative_link() == '/'
    selenium.find_element(By.XPATH, '//h2').click()
    selenium.find_element(By.XPATH, '//span[contains(text(), "Выйти")]').click()   


def test_auth_start_page_email(selenium):
    """
    13. Продукт Старт web. Авторизация. Позитивный     
    """
    page = AuthStartPage(selenium)
    page.enter_email(email)
    page.enter_pass(password)
    page.btn_click()

    assert page.get_relative_link() == '/'
    selenium.find_element(By.XPATH, '//h2').click()
    selenium.find_element(By.XPATH, '//span[contains(text(), "Выйти")]').click()


def test_auth_start_page_email_incorrect(selenium):
    """
    14. Продукт Старт web. Авторизация. Негативный    
    """
    page = AuthStartPage(selenium)
    page.enter_email("Albuquerque@gmail.com")
    page.enter_pass(password)
    page.btn_click()

    assert selenium.find_element(By.ID, "form-error-message")


def test_auth_smarthome_page_email(selenium):
    """
    15. Продукт Умный дом web. Авторизация. Позитивный 
    """
    page = AuthSmarthomePage(selenium)
    page.enter_email(email)
    page.enter_pass(password)
    page.btn_click()

    assert selenium.find_element(By.CLASS_NAME, "profileLinkIcon___3flTM")
    selenium.find_element(By.CLASS_NAME, "profileLinkIcon___3flTM").click()
    selenium.find_element(By.XPATH, '//span[contains(text(), "Выйти")]').click()


def test_auth_smarthome_page_phone(selenium):
    """
    16. Продукт Умный дом web. Авторизация. Позитивный     
    """
    page = AuthSmarthomePage(selenium)
    page.enter_email(phone)
    page.enter_pass(password)
    page.btn_click()

    assert selenium.find_element(By.CLASS_NAME, "profileLinkIcon___3flTM")
    selenium.find_element(By.CLASS_NAME, "profileLinkIcon___3flTM").click()
    selenium.find_element(By.XPATH, '//span[contains(text(), "Выйти")]').click()


def test_auth_smarthome_page_email_incorrect(selenium):
    """
    17. Продукт Умный дом web. Авторизация. Негативный    
    """
    page = AuthSmarthomePage(selenium)
    page.enter_email("Albuquerque@gmail.com")
    page.enter_pass(password)
    page.btn_click()

    assert selenium.find_element(By.ID, "form-error-message")


def test_auth_key_page_phone(selenium):
    """
    18. Продукт Ключ web. Авторизация. Позитивный    
    """
    page = AuthKeyPage(selenium)
    page.enter_email(phone)
    page.enter_pass(password)
    page.btn_click()

    assert page.get_relative_link() == '/'
    selenium.find_element(By.XPATH, '//h2').click()
    selenium.find_element(By.XPATH, '//span[contains(text(), "Выйти")]').click()   


def test_auth_key_page_email(selenium):
    """
    19. Продукт Ключ web. Авторизация. Позитивный    
    """
    page = AuthKeyPage(selenium)
    page.enter_email(email)
    page.enter_pass(password)
    page.btn_click()

    assert page.get_relative_link() == '/'
    selenium.find_element(By.XPATH, '//h2').click()
    selenium.find_element(By.XPATH, '//span[contains(text(), "Выйти")]').click()


def test_auth_key_page_email_incorrect(selenium):
    """
    20. Продукт Ключ web. Авторизация. Негативный    
    """
    page = AuthKeyPage(selenium)
    page.enter_email("Albuquerque@gmail.com")
    page.enter_pass(password)
    page.btn_click()

    assert selenium.find_element(By.ID, "form-error-message")