from behave import *
from acceptance_tests.page_model.base_page import BasePage
from acceptance_tests.page_model.pricing_page import PricingPage

# to avoid hardcoding
use_step_matcher('re')

#---------------------------------then

@then("The header is present on page")
def step_impl(context):
    pp = PricingPage(context.driver)
    assert pp.pricing_header().is_displayed()

@step('The pricing header has content: "(.*)"')
def step_impl(context, content):
    pp = PricingPage(context.driver)
    assert pp.pricing_header().text == content

@step('The page title has content: "(.*)"')
def step_impl(context, content):
    bp = BasePage(context.driver)
    assert content in bp.get_title()