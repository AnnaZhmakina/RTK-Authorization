from .base_page import BasePage, BaseOnlimePage, BaseStartPage, BaseSmarthomePage, BaseKeyPage
from .locators import AuthLocators, RegLocators, AuthOnlimeLocators, AuthStartLocators, AuthSmarthomeLocators, AuthKeyLocators
import time


class AuthPage(BasePage):
    def __init__(self, driver,timeout=10):
        super().__init__(driver, timeout)
        time.sleep(5)
        self.phone = driver.find_element(*AuthLocators.AUTH_PHONE)   
        self.email = driver.find_element(*AuthLocators.AUTH_EMAIL)
        self.login = driver.find_element(*AuthLocators.AUTH_LOGIN)
        self.lc = driver.find_element(*AuthLocators.AUTH_LOGIN)
        self.password = driver.find_element(*AuthLocators.AUTH_PASS)
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
        time.sleep(5)


    def enter_phone(self, value):
        self.phone.send_keys(value)


    def enter_email(self, value):
        self.email.send_keys(value)


    def enter_login(self, value):
        self.login.send_keys(value)


    def enter_lc(self, value):
        self.lc.send_keys(value)
        
    
    def enter_pass(self, value):
        self.password.send_keys(value)
    
    
    def btn_click(self):
        self.btn.click()




class RegPage(BasePage):
    def __init__(self, driver,timeout=10):
        super().__init__(driver, timeout)
        time.sleep(5) 
        self.btn_to_reg = driver.find_element(*RegLocators.TO_REG_BTN).click()
        time.sleep(5)
        self.name = driver.find_element(*RegLocators.REG_NAME)
        self.surname = driver.find_element(*RegLocators.REG_SURNAME)
        self.email = driver.find_element(*RegLocators.REG_EMAIL_PHONE)
        self.phone = driver.find_element(*RegLocators.REG_EMAIL_PHONE)
        self.password = driver.find_element(*RegLocators.REG_PASS)
        self.password_confirm = driver.find_element(*RegLocators.REG_PASS_CONFIRM)
        self.btn = driver.find_element(*RegLocators.REG_BTN)


    def enter_name(self, value):
        self.name.send_keys(value)


    def enter_surname(self, value):
        self.surname.send_keys(value)
        
        
    def enter_email(self, value):
        self.email.send_keys(value)


    def enter_phone(self, value):
        self.phone.send_keys(value)
        

    def enter_pass(self, value):
        self.password.send_keys(value)


    def enter_pass_confirm(self, value):
        self.password_confirm.send_keys(value)
        

    def btn_click(self):
        self.btn.click()


class AuthOnlimePage(BaseOnlimePage):
    def __init__(self, driver,timeout=10):
        super().__init__(driver, timeout)
        time.sleep(5)
        self.standart_auth_btn = driver.find_element(*AuthOnlimeLocators.STANDART_AUTH_BTN).click()
        time.sleep(5)
        self.email = driver.find_element(*AuthOnlimeLocators.AUTH_EMAIL)
        self.password = driver.find_element(*AuthOnlimeLocators.AUTH_PASS)
        self.auth_btn = driver.find_element(*AuthOnlimeLocators.AUTH_BTN)


    def enter_email(self, value):
        self.email.send_keys(value)


    def enter_pass(self, value):
        self.password.send_keys(value)    


    def standart_btn_click(self):
        self.standart_auth_btn.click()
        
        
    def btn_click(self):
        self.auth_btn.click()


class AuthStartPage(BaseStartPage):
    def __init__(self, driver,timeout=10):
        super().__init__(driver, timeout)
        time.sleep(5)
        self.standart_auth_btn = driver.find_element(*AuthStartLocators.STANDART_AUTH_BTN).click()
        time.sleep(5)
        self.email = driver.find_element(*AuthStartLocators.AUTH_EMAIL)
        self.password = driver.find_element(*AuthStartLocators.AUTH_PASS)
        self.auth_btn = driver.find_element(*AuthStartLocators.AUTH_BTN)


    def enter_email(self, value):
        self.email.send_keys(value)


    def enter_pass(self, value):
        self.password.send_keys(value)


    def standart_btn_click(self):
        self.standart_auth_btn.click()


    def btn_click(self):
        self.auth_btn.click()


class AuthSmarthomePage(BaseSmarthomePage):
    def __init__(self, driver,timeout=10):
        super().__init__(driver, timeout)
        time.sleep(5)
        self.standart_auth_btn = driver.find_element(*AuthSmarthomeLocators.STANDART_AUTH_BTN).click()
        time.sleep(5)
        self.email = driver.find_element(*AuthSmarthomeLocators.AUTH_EMAIL)
        self.password = driver.find_element(*AuthSmarthomeLocators.AUTH_PASS)
        self.auth_btn = driver.find_element(*AuthSmarthomeLocators.AUTH_BTN)


    def enter_email(self, value):
        self.email.send_keys(value)


    def enter_pass(self, value):
        self.password.send_keys(value)


    def standart_btn_click(self):
        self.standart_auth_btn.click()


    def btn_click(self):
        self.auth_btn.click()


class AuthKeyPage(BaseKeyPage):
    def __init__(self, driver,timeout=10):
        super().__init__(driver, timeout)
        time.sleep(5)
        self.enter_btn = driver.find_element(*AuthKeyLocators.ENTER_BTN).click()
        time.sleep(5)
        self.standart_auth_btn = driver.find_element(*AuthKeyLocators.STANDART_AUTH_BTN).click()
        time.sleep(5)
        self.email = driver.find_element(*AuthKeyLocators.AUTH_EMAIL)
        self.password = driver.find_element(*AuthKeyLocators.AUTH_PASS)
        self.auth_btn = driver.find_element(*AuthKeyLocators.AUTH_BTN)


    def enter_email(self, value):
        self.email.send_keys(value)


    def enter_pass(self, value):
        self.password.send_keys(value)


    def standart_btn_click(self):
        self.standart_auth_btn.click()


    def btn_click(self):
        self.auth_btn.click()