from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.product_search_page import ProductSearchPage


# Positive test case
def test_search_product_valid(android_driver):
    login_page = LoginPage(android_driver)
    login_page.select_germany()
    login_page.select_english()
    login_page.agree()
    login_page.go_to_login()
    login_page.login('test@automation.com', 'Qwerty1Z!')
    login_page.skip()
    product_search_page = ProductSearchPage(android_driver)
    product_search_page.search_product("Paracetamol")
    assert product_search_page.is_search_result_displayed_for("Paracetamol"), "Search result is not displayed"
    cart_page = CartPage(android_driver)
    cart_page.add_to_cart()
    assert cart_page.is_product_added(), "Product is not added to cart"
    assert cart_page.is_go_to_cart_button_displayed(), "Go to cart button is not displayed"
    # TODO: Change quantity of the product, and proceed to checkout



