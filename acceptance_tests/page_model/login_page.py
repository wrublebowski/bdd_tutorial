from acceptance_tests.page_model.base_page import BasePage
from acceptance_tests.locators.login_locators import LoginPageLocators


class LoginPage(BasePage):
# __init__ method also inherited from BasePage

    def login_URL(self):
        return "https://app.pushpushgo.com/login?language=en"

    def get_email_field(self):
        return self.driver.find_element(*LoginPageLocators._email_field)

    def get_password_field(self):
        return self.driver.find_element(*LoginPageLocators._password_field)

    # def click_login(self):
    #     self.click_element(*LoginPageLocators._login_link)