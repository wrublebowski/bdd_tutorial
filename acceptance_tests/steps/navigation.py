from behave import *
from selenium import webdriver

from acceptance_tests.page_model.home_page import HomePage
from acceptance_tests.page_model.pricing_page import PricingPage
from acceptance_tests.page_model.login_page import LoginPage

# to avoid hardcoding
use_step_matcher('re')

#---------------------------------given

@given("I start on the homepage")
def step_impl(context):
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    context.driver = webdriver.Chrome(chrome_options=chrome_options)
    hp = HomePage(context.driver)
    context.driver.get(hp.homeUrl())

@given("I start on pricing page")
def step_impl(context):
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    context.driver = webdriver.Chrome(chrome_options=chrome_options)
    pp = PricingPage(context.driver)
    context.driver.get(pp.pricingUrl())

#---------------------------------then

@then("Im in pricing page")
def step_impl(context):
    pp = PricingPage(context.driver)
    expected_url = pp.pricingUrl()
    assert context.driver.current_url == expected_url

@then("Im on login page")
def step_impl(context):
    lp = LoginPage(context.driver)
    expected_url = lp.loginUrl()
    assert context.driver.current_url == expected_url