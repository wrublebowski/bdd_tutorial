# use locators to form methods

from acceptance_tests.locators.home_locators import HomePageLocators
from acceptance_tests.page_model.base_page import BasePage


class HomePage(BasePage):
# __init__ method also inherited from BasePage

    def homeUrl(self):
        return self.baseUrl() + "/"

    def getPricingLink(self):
        return self.driver.find_element(*HomePageLocators._pricing_link)

    def getHomeHeader(self):
        return self.driver.find_element(*HomePageLocators._home_header)