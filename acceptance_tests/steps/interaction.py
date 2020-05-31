from behave import *
from selenium.webdriver.common.by import By
from acceptance_tests.page_model.base_page import BasePage

# to avoid hardcoding
use_step_matcher('re')

#---------------------------------when

@when('I click on link with text: "(.*)"')
def step_impl(context, link_text):
    bp = BasePage(context.driver)
    links = bp.naviLinks()
    # searching for matching link text
    matching_links = [l for l in links if l.text == link_text]
    if len(matching_links) >0:
        matching_links[0].click()
    else:
        raise RuntimeError

@step('Scroll page by "(.*)"')
def step_impl(context, distance):
    bp = BasePage(context.driver)
    bp.scrollPage(distance)