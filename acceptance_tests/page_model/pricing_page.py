from acceptance_tests.locators.pricing_locators import PricingPageLocators
from acceptance_tests.page_model.base_page import BasePage

class PricingPage(BasePage):
# __init__ method also inherited from BasePage

    def pricing_URL(self):
        return self.base_URL() + "/pages/pricing/"

    def pricing_header(self):
        return self.driver.find_element(*PricingPageLocators._pricing_header)

    def contact_us_btn(self):
        return self.driver.find_element(*PricingPageLocators._contactus_btn)

    def choose_btn(self):
        return self.driver.find_element(*PricingPageLocators._choose_btn)