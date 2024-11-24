from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    ADD_TO_CART_BUTTON = (By.XPATH, '//android.widget.Button[@text="Add to cart"]')
    ADDED_TO_CART_MESSAGE = (By.XPATH, '//android.widget.TextView[@text="Added to cart"]')
    GO_TO_CART_BUTTON = (By.XPATH, '//android.widget.Button[@text="Go to cart"]')


    def add_to_cart(self):
        self.get(self.ADD_TO_CART_BUTTON).click()

    def is_product_added(self):
        return self.get(self.ADDED_TO_CART_MESSAGE).is_displayed()

    def is_go_to_cart_button_displayed(self):
        return self.get(self.GO_TO_CART_BUTTON).is_displayed()

