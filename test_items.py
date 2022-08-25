import pytest
from selenium.webdriver.common.by import By
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_submit_button_visibility(browser):
    browser.get(link)
    assert len(browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")) > 0, "No button for submitting to the basket found on the page"
