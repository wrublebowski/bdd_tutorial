from selenium.webdriver.common.by import By

class PricingPageLocators():
    # locators in tuples
    _pricing_header = By.XPATH, "//h1[contains(text(),'Pricing')]"
    _choose_btn = By.LINK_TEXT, "Choose"
    _contactus_btn = By.LINK_TEXT, "Contact us"