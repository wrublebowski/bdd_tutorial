from behave import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from acceptance_tests.locators.pricing_locators import PricingPageLocators

# use_step_matcher('re')

@step('Wait for choose_btn to load')
def step_impl(context):
    WebDriverWait(context.driver, timeout=5).until(
        expected_conditions.visibility_of_element_located(PricingPageLocators._choose_btn)) # provide unpacked tuple