from acceptance_tests.locators.pricing_locators import PricingPageLocators
from acceptance_tests.page_model.base_page import BasePage

class PricingPage(BasePage):
# __init__ method also inherited from BasePage

    def pricingUrl(self):
        return self.baseUrl() + "/pages/pricing/"

    def pricingHeader(self):
        return self.driver.find_element(*PricingPageLocators._pricing_header)

    def contactusBtn(self):
        return self.driver.find_element(*PricingPageLocators._contactus_btn)

    def chooseBtn(self):
        return self.driver.find_element(*PricingPageLocators._choose_btn)