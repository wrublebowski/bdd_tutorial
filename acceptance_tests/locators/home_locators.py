from selenium.webdriver.common.by import By

class HomePageLocators():
    # locators in tuples
    _home_header = By.XPATH, "//h1[contains(text(),'Generate traffic and increase profits')]"
    _pricing_link = By.XPATH,  "//a[contains(text(),'Pricing')]"
    _login_link = By.XPATH, "//a[contains(text(),'Sign in')]"
