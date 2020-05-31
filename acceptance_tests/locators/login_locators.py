from selenium.webdriver.common.by import By

class LoginPageLocators:

    _email_field = By.XPATH, "//input[@id='t-login-username']"
    _password_field = By.XPATH, "//input[@id='t-login-password']"
    _login_btn = By.XPATH, '//input[@class="button-primary float-right app-login-submit"]'