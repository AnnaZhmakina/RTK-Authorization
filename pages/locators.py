from selenium.webdriver.common.by import By

class AuthLocators:
    AUTH_PHONE = (By.ID, "username")
    AUTH_EMAIL = (By.ID, "username")
    AUTH_LOGIN = (By.ID, "username")
    AUTH_PASS = (By.ID, "password")
    AUTH_BTN = (By.ID, "kc-login")
    GET_CODE_BTN = (By.ID, "otp_get_code")

    
class RegLocators:
    REG_NAME = (By.XPATH, '//*[@name="firstName"]')
    REG_SURNAME = (By.XPATH, '//*[@name="lastName"]')
    REG_EMAIL_PHONE = (By.ID, "address")
    REG_PASS = (By.ID, "password")
    REG_PASS_CONFIRM = (By.ID, "password-confirm")
    TO_REG_BTN = (By.ID, "kc-register")
    REG_BTN = (By.XPATH, '//button')
    
    
class AuthOnlimeLocators:
    STANDART_AUTH_BTN = (By.ID, "standard_auth_btn")
    AUTH_EMAIL = (By.ID, "username")
    AUTH_PASS = (By.ID, "password")
    AUTH_BTN = (By.ID, "kc-login")
    
    
class AuthStartLocators:
    STANDART_AUTH_BTN = (By.ID, "standard_auth_btn")
    AUTH_EMAIL = (By.ID, "username")
    AUTH_PASS = (By.ID, "password")
    AUTH_BTN = (By.ID, "kc-login")


class AuthSmarthomeLocators:
    STANDART_AUTH_BTN = (By.ID, "standard_auth_btn")
    AUTH_EMAIL = (By.ID, "username")
    AUTH_PASS = (By.ID, "password")
    AUTH_BTN = (By.ID, "kc-login")


class AuthKeyLocators:
    ENTER_BTN = (By.XPATH, '//*[@class="go_kab"]')
    STANDART_AUTH_BTN = (By.ID, "standard_auth_btn")
    AUTH_EMAIL = (By.ID, "username")
    AUTH_PASS = (By.ID, "password")
    AUTH_BTN = (By.ID, "kc-login")
