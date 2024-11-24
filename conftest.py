import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
import pytest


def create_android_driver(custom_opts=None):
    """Create and return an Android WebDriver instance."""
    options = UiAutomator2Options() # Update this based on your device
    options.deviceName = get_android_device_name()
    options.full_reset = True
    options.automationName = 'UiAutomator2'
    options.app = os.path.join("apk/app.apk")
    options.newCommandTimeout = 9999

    if custom_opts:
        options.load_capabilities(custom_opts)

    # Return the WebDriver instance
    return webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)


@pytest.fixture
def android_driver():
    """Fixture for creating an Android driver with default options."""
    driver = create_android_driver()
    yield driver
    driver.quit()


def get_android_device_name():
    """Retrieve the Android device name using a system command."""
    ANDROID_DEVICE_NAME = "adb devices -l | grep 'model' | awk '{print $1}'"  # Example command
    device_name = os.popen(ANDROID_DEVICE_NAME).read().strip()
    return device_name
