import pytest
from pages.login_page import LoginPage
from pages.product_search_page import ProductSearchPage


# Positive test case

@pytest.mark.parametrize('query', ['Paracetamol', 'Aspirin'])
def test_search_product_valid(android_driver, query):
    login_page = LoginPage(android_driver)
    login_page.select_germany()
    login_page.select_english()
    login_page.agree()
    login_page.go_to_login()
    login_page.login('test@automation.com', 'Qwerty1Z!')
    login_page.skip()
    product_search_page = ProductSearchPage(android_driver)
    product_search_page.search_product(query)
    assert product_search_page.is_search_result_displayed_for(query), "Search result is not displayed"


# Negative test cases
def test_search_product_invalid(android_driver):
    login_page = LoginPage(android_driver)
    login_page.select_germany()
    login_page.select_english()
    login_page.agree()
    login_page.go_to_login()
    login_page.login('test@automation.com', 'Qwerty1Z!')
    login_page.skip()
    product_search_page = ProductSearchPage(android_driver)
    product_search_page.search_product('invalid')
    assert product_search_page.is_0_result_shown(), "0 result is not shown"
