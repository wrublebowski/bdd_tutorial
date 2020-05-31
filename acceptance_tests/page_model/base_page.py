from acceptance_tests.locators.base_locators import BasePageLocators

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