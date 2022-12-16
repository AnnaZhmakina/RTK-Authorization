from selenium.webdriver.common.by import By
import time
from pages.pages import AuthPage, RegPage, AuthOnlimePage, AuthStartPage, AuthSmarthomePage, AuthKeyPage
from pages.config import long_name_259, long_phone_259, long_password_259, phone, email, password, lc

#запуск тестов из консоли:
#pytest -v --driver Chrome --driver-path ./chromedriver.exe  tests/test_pages.py


#Продукт ЕЛК web. Регистрация. Позитивный (bug)
#1
def test_reg_page_boundary_values_names_passwords(selenium):
    page = RegPage(selenium)
    page.enter_name("А-")
    page.enter_surname("Ф-")
    page.enter_email("abcd@mail.ru")
    page.enter_pass("yV6vdvMi")
    page.enter_pass_confirm("yV6vdvMi")
    page.btn_click()

    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'
    assert selenium.find_element(By.ID, "rt-code-0")


#Продукт ЕЛК web. Регистрация. Негативный
#2
def test_reg_page_empty_values(selenium):
    page = RegPage(selenium)
    time.sleep(5) #ждем реакции
    page.enter_name("")
    page.enter_surname("")
    page.enter_email("")
    page.enter_pass("")
    page.enter_pass_confirm("")
    page.btn.click()

    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'


#Продукт ЕЛК web. Регистрация. Негативный
#3
def test_reg_page_boundary_values_names_30_and_not_confirm(selenium):
    page = RegPage(selenium)
    page.enter_name("")
    page.enter_surname("Через-Забор-Ногу-Задирищенский")
    page.enter_email("Через-Забор-Ногу-Задирищенский")
    page.enter_pass("Ww123456")
    page.enter_pass_confirm("Ww12345")
    page.btn_click()

    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'


#Продукт ЕЛК web. Регистрация. Негативный
#4
def test_reg_page_boundary_values_259(selenium):
    page = RegPage(selenium)
    page.enter_name(long_name_259)
    page.enter_surname(long_name_259)
    page.enter_phone(long_phone_259)
    page.enter_pass(long_password_259)
    page.enter_pass_confirm(long_password_259)
    page.btn_click()

    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'


#Продукт ЕЛК web. Авторизация. Позитивный
#5
def test_auth_elk_page_phone(selenium):
    page = AuthPage(selenium)
    page.enter_phone(phone)
    page.enter_pass(password)
    page.btn_click()

    assert page.get_relative_link() == '/account_b2c/page'
    selenium.find_element(By.ID, "logout-btn").click()


#Продукт ЕЛК web. Авторизация. Позитивный
#6
def test_auth_elk_page_email(selenium):
    page = AuthPage(selenium)
    page.enter_email(email)
    page.enter_pass(password)
    page.btn_click()

    assert page.get_relative_link() == '/account_b2c/page'
    selenium.find_element(By.ID, "logout-btn").click()


#Продукт ЕЛК web. Авторизация. Позитивный
#7
def test_auth_elk_page_lc(selenium):
    page = AuthPage(selenium)
    page.enter_lc(lc)
    page.enter_pass(password)
    page.btn_click()

    assert page.get_relative_link() == '/account_b2c/page'
    selenium.find_element(By.ID, "logout-btn").click()


#Продукт ЕЛК web. Авторизация. Негативный
#8
def test_auth_elk_page_phone_symbols(selenium):
    page = AuthPage(selenium)
    page.enter_phone("абвгд")
    page.enter_pass(password)
    page.btn_click()

    assert page.get_relative_link() == '/account_b2c/page'


#Продукт Онлайм web. Авторизация. Позитивный
#9 
def test_auth_onlime_page_phone(selenium):
    page = AuthOnlimePage(selenium)
    page.enter_email(phone)
    page.enter_pass(password)
    page.btn_click()

    assert page.get_relative_link() == '/account_b2c/page'
    selenium.find_element(By.ID, "logout-btn").click()


#Продукт Онлайм web. Авторизация. Позитивный
#10 
def test_auth_onlime_page_email(selenium):
    page = AuthOnlimePage(selenium)
    page.enter_email(email)
    page.enter_pass(password)
    page.btn_click()

    assert page.get_relative_link() == '/account_b2c/page'
    selenium.find_element(By.ID, "logout-btn").click()


#Продукт Онлайм web. Авторизация. Негативный
#11 
def test_auth_onlime_page_email_incorrect(selenium):
    page = AuthOnlimePage(selenium)
    page.enter_email("Albuquerque@gmail.com")
    page.enter_pass(password)
    page.btn_click()

    assert selenium.find_element(By.ID, "form-error-message")


#Продукт Старт web. Авторизация. Позитивный
#12
def test_auth_start_page_phone(selenium):
    page = AuthStartPage(selenium)
    page.enter_email(phone)
    page.enter_pass(password)
    page.btn_click()

    assert page.get_relative_link() == '/'
    selenium.find_element(By.XPATH, '//h2').click()
    selenium.find_element(By.XPATH, '//span[contains(text(), "Выйти")]').click()   


#Продукт Старт web. Авторизация. Позитивный
#13
def test_auth_start_page_email(selenium):
    page = AuthStartPage(selenium)
    page.enter_email(email)
    page.enter_pass(password)
    page.btn_click()

    assert page.get_relative_link() == '/'
    selenium.find_element(By.XPATH, '//h2').click()
    selenium.find_element(By.XPATH, '//span[contains(text(), "Выйти")]').click()


#Продукт Старт web. Авторизация. Негативный
#14
def test_auth_start_page_email_incorrect(selenium):
    page = AuthStartPage(selenium)
    page.enter_email("Albuquerque@gmail.com")
    page.enter_pass(password)
    page.btn_click()

    assert selenium.find_element(By.ID, "form-error-message")


#Продукт Умный дом web. Авторизация. Позитивный
#15
def test_auth_smarthome_page_email(selenium):
    page = AuthSmarthomePage(selenium)
    page.enter_email(email)
    page.enter_pass(password)
    page.btn_click()

    assert selenium.find_element(By.CLASS_NAME, "profileLinkIcon___3flTM")
    selenium.find_element(By.CLASS_NAME, "profileLinkIcon___3flTM").click()
    selenium.find_element(By.XPATH, '//span[contains(text(), "Выйти")]').click()


#Продукт Умный дом web. Авторизация. Позитивный
#16
def test_auth_smarthome_page_phone(selenium):
    page = AuthSmarthomePage(selenium)
    page.enter_email(phone)
    page.enter_pass(password)
    page.btn_click()

    assert selenium.find_element(By.CLASS_NAME, "profileLinkIcon___3flTM")
    selenium.find_element(By.CLASS_NAME, "profileLinkIcon___3flTM").click()
    selenium.find_element(By.XPATH, '//span[contains(text(), "Выйти")]').click()



#Продукт Умный дом web. Авторизация. Негативный
#17
def test_auth_smarthome_page_email_incorrect(selenium):
    page = AuthSmarthomePage(selenium)
    page.enter_email("Albuquerque@gmail.com")
    page.enter_pass(password)
    page.btn_click()

    assert selenium.find_element(By.ID, "form-error-message")



#Продукт Ключ web. Авторизация. Позитивный
#18
def test_auth_key_page_phone(selenium):
    page = AuthKeyPage(selenium)
    page.enter_email(phone)
    page.enter_pass(password)
    page.btn_click()

    assert page.get_relative_link() == '/'
    selenium.find_element(By.XPATH, '//h2').click()
    selenium.find_element(By.XPATH, '//span[contains(text(), "Выйти")]').click()   


#Продукт Ключ web. Авторизация. Позитивный
#19
def test_auth_key_page_email(selenium):
    page = AuthKeyPage(selenium)
    page.enter_email(email)
    page.enter_pass(password)
    page.btn_click()

    assert page.get_relative_link() == '/'
    selenium.find_element(By.XPATH, '//h2').click()
    selenium.find_element(By.XPATH, '//span[contains(text(), "Выйти")]').click()


#Продукт Ключ web. Авторизация. Негативный
#20
def test_auth_key_page_email_incorrect(selenium):
    page = AuthKeyPage(selenium)
    page.enter_email("Albuquerque@gmail.com")
    page.enter_pass(password)
    page.btn_click()

    assert selenium.find_element(By.ID, "form-error-message")