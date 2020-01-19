import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import os

class BasicTests(unittest.TestCase):
    def test_brooks_running_add_product_tocart(self):
        search_query = "launch"
        chromedriver_path = os.environ['USERPROFILE'] + "\\SeleniumWebDrivers\\chromedriver.exe"
        chrome = webdriver.Chrome(executable_path=chromedriver_path)
        chrome.implicitly_wait(10)
        chrome.get("https://www.brooksrunning.com/")
        chrome.set_window_size(1440, 1080)
        # reload the website to avoid firtload defect
        chrome.get("https://www.brooksrunning.com/")
        chrome.set_window_size(1440, 1080)
        # Search products using search_query
        search_icon = chrome.find_element_by_css_selector('#site-search')
        search_icon.click()
        search_box = chrome.find_element_by_css_selector('#q')
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.ENTER)
        # Select the second item in search results list
        result = chrome.find_elements(By.CSS_SELECTOR, ".o-block--related-product__product-card")
        result[1].click()
        # In product page, select size and add product to cart
        select_box = chrome.find_element(By.CLASS_NAME, "cs-select--product-size")
        ActionChains(chrome).move_to_element(select_box).click(select_box).perform()
        sizesoption = chrome.find_elements(By.CSS_SELECTOR, "li.cs-select--product-size .cs-options li")
        sizesoption[1].click()
        ActionChains(chrome).move_to_element(chrome.find_element_by_id('add-to-cart')).perform()
        chrome.find_element_by_id('add-to-cart').click()
        # Go to Cart page and check if the quantity is correct (should show 1)
        WebDriverWait(chrome, 10).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".cta-group button.a-btn--primary")))
        chrome.find_element(By.CSS_SELECTOR, ".cta-group button.a-btn--primary").click()
        qual = Select(chrome.find_element_by_css_selector('#quantity'))
        assert qual.first_selected_option.text == '1'
        chrome.close()