
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductSearchPage(BasePage):
    SEARCH_FIELD = (By.XPATH, '//android.widget.TextView[@resource-id="et_search_placeholder"]')
    ZERO_RESULT = (By.XPATH, '//android.widget.TextView[@text="0 results"]')

    def search_product(self, product_name):
        search_field = self.get(self.SEARCH_FIELD).click()
        search_field.click()
        search_field.send_keys(product_name)

    def is_search_result_displayed_for(self, query):
        SEARCH_RESULT = (By.XPATH, f'//android.widget.TextView[@resource-id="tv_name" and @text="{query}"]')
        return self.get(SEARCH_RESULT).is_displayed()

    def is_0_result_shown(self):
        return self.get(self.ZERO_RESULT).is_displayed()





