from time import sleep

from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    EMAIL_FIELD = (By.XPATH, '(//android.widget.TextView[@text="E-mail address"])[last()]')
    PASSWORD_FIELD = (By.XPATH, '//android.widget.EditText[@resource-id="ti_password"]')
    LOGIN_BUTTON = (By.XPATH, '(//android.view.View[@resource-id="btn_login"])[2]/android.widget.Button')
    GERMANY_BUTTON = (By.XPATH, '//android.view.View[@resource-id="mcv_item_DE"]/android.view.View')
    ENGLISH_BUTTON = (By.XPATH, '//android.view.View[@resource-id="mcv_item_en"]/android.view.View')
    AGREE_BUTTON = (By.XPATH, '//android.widget.TextView[@text="Agree"]')
    LOGIN_OPTION_BUTTON = (By.XPATH, '//android.view.View[@resource-id="btn_login"]/android.widget.Button')
    SKIP_BUTTON = (By.XPATH, '//android.widget.TextView[@text="Skip"]')
    HELLO_MESSAGE = (By.XPATH, '//android.widget.TextView[@resource-id="tv_home_welcome_title"]')
    NAV_BAR = (By.XPATH, '//android.widget.FrameLayout[@resource-id="shop.shop_apotheke.com.shopapotheke.debug:id/bnv_navigation_bar"]')
    CHECK_EMAIL_TEXT = (By.XPATH, '//android.widget.TextView[@text="Check e-mail address"]')
    CHECK_PASSWORD_TEXT = (By.XPATH, '//android.widget.TextView[@text="Check password"]')
    def select_germany(self):
        sleep(5)
        self.get(self.GERMANY_BUTTON).click()

    def select_english(self):
        sleep(5)
        self.get(self.ENGLISH_BUTTON).click()

    def agree(self):
        sleep(5)
        self.get(self.AGREE_BUTTON).click()

    def go_to_login(self):
        sleep(5)
        self.get(self.LOGIN_OPTION_BUTTON).click()


    def login(self, username, password):
        sleep(5)
        email = self.get(self.EMAIL_FIELD)
        email.click()
        sleep(3)
        email.send_keys(username)
        sleep(5)
        password = self.get(self.PASSWORD_FIELD)
        password.click()
        password.send_keys(password)

        self.get(self.LOGIN_BUTTON).click()

    def skip(self):
        self.get(self.SKIP_BUTTON).click()

    def is_hello_message_displayed(self):
        sleep(5)
        return self.get(self.HELLO_MESSAGE).is_displayed()

    def is_navigation_bar_shown(self):
        sleep(5)
        return self.get(self.NAV_BAR).is_displayed()

    def is_incorrect_email_message_displayed(self):
        sleep(5)
        return self.get(self.CHECK_EMAIL_TEXT).is_displayed()

    def is_incorrect_password_message_displayed(self):
        sleep(5)
        return self.get(self.CHECK_PASSWORD_TEXT).is_displayed()


