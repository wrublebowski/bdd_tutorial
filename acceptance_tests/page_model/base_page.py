from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from acceptance_tests.locators.base_locators import BasePageLocators
from acceptance_tests.locators.login_locators import LoginPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def base_URL(self):
        return "https://pushpushgo.com/en"   # no ending slash '/'

    def get_title(self):
        return self.driver.title

    def navi_links_list(self):
        return self.driver.find_elements(*BasePageLocators._nav_links)

    def scroll_page(self, distance):
        return self.driver.execute_script(f"window.scrollBy(0, {distance});")

    def buttons_list(self):
        return self.driver.find_elements(*BasePageLocators._buttons)

    def wait_for_element(self, locator):
        WebDriverWait(self.driver, timeout=15).until(
            expected_conditions.visibility_of_element_located(locator))  # provide unpacked tuple

    def click_element(self, locatorType, locator):
        self.driver.find_element(locatorType, locator).click()