from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from acceptance_tests.locators.base_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def base_URL(self):
        '''
        :return: base URL, notice no ending slash
        '''
        return "https://pushpushgo.com/en"

    def get_title(self):
        '''
        :return: title of a current URL
        '''
        return self.driver.title

    def navi_links_list(self):
        '''
        returns list of navi links
        '''
        return self.driver.find_elements(*BasePageLocators._nav_links)

    def scroll_page(self, distance):
        '''
        distance: int
        Scrolls down current page by <distance> pixels.
        For scrolling up provide negative integer
        '''
        return self.driver.execute_script(f"window.scrollBy(0, {distance});")

    def buttons_list(self):
        '''
        :return: List of buttons, elements with class name 'btn'
        '''
        return self.driver.find_elements(*BasePageLocators._buttons)

    def wait_for_element(self, locator):
        '''
        waits for element
        :param locator: tuple with no *
        '''
        WebDriverWait(self.driver, timeout=15).until(
            expected_conditions.visibility_of_element_located(locator))  # provide unpacked tuple

    def click_element(self, locatorType, locator):
        '''
        clicks on element
        as arguments you provide *tuple
        '''
        self.driver.find_element(locatorType, locator).click()