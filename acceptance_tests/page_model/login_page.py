from acceptance_tests.page_model.base_page import BasePage
from acceptance_tests.locators.login_locators import LoginPageLocators


class LoginPage(BasePage):
# __init__ method also inherited from BasePage

    def login_URL(self):
        return "https://app.pushpushgo.com/login?language=en"