from acceptance_tests.locators.base_locators import BasePageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def baseUrl(self):
        return "https://pushpushgo.com/en"   # no ending slash '/'

    def getTitle(self):
        return self.driver.title

    def naviLinks(self):
        return self.driver.find_elements(*BasePageLocators._nav_links)

    def scrollPage(self, distance):
        return self.driver.execute_script(f"window.scrollBy(0, {distance});")