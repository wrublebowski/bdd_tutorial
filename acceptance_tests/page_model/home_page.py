# use locators to form methods

from acceptance_tests.locators.home_locators import HomePageLocators
from acceptance_tests.page_model.base_page import BasePage


class HomePage(BasePage):
# __init__ method also inherited from BasePage

    def home_URL(self):
        return self.base_URL() + "/"

    def get_pricing_link(self):
        return self.driver.find_element(*HomePageLocators._pricing_link)

    def get_home_header(self):
        return self.driver.find_element(*HomePageLocators._home_header)