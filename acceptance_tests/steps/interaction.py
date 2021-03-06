from behave import *
from acceptance_tests.locators.login_locators import LoginPageLocators
from acceptance_tests.page_model.base_page import BasePage
from acceptance_tests.page_model.login_page import LoginPage

# to avoid hardcoding


use_step_matcher('re')

#---------------------------------when

@step('I click on navigation link with text: "(.*)"')
def step_impl(context, link_text):
    bp = BasePage(context.driver)
    links = bp.navi_links_list()
    # searching for matching link text
    matching_links = [l for l in links if l.text.lower() == link_text.lower()]
    if len(matching_links) >0:
        matching_links[0].click()
    else:
        raise RuntimeError

@then('I click on button with text: "(.*)"')
def step_impl(context, btn_text):
    bp = BasePage(context.driver)
    buttons = bp.buttons_list()
    # searching for matching link text
    matching_buttons = [b for b in buttons if b.text.lower() == btn_text.lower()]
    if len(matching_buttons) >0:
        matching_buttons[0].click()
    else:
        raise RuntimeError

@step('Scroll page by "(.*)"')
def step_impl(context, distance):
    bp = BasePage(context.driver)
    bp.scroll_page(distance)

@then('Login with email "(.*)" and password "(.*)"')
def step_impl(context, email, password):
    # bp = BasePage(context.driver)
    lp = LoginPage(context.driver)
    lp.wait_for_element(LoginPageLocators._email_field)
    lp.sign_in(email, password)