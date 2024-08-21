import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.home_page__locators import ACCORDION_MAIN, ACCORDION_PANEL_MAIN, ORDER_BUTTON_TOP, ORDER_BUTTON_BOTTOM


class Homepagescooter:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_home_page(self):

        WebDriverWait(self.driver, 100).until(
            expected_conditions.visibility_of_element_located ((By.CSS_SELECTOR , ACCORDION_MAIN)))

    def click_accordion_item(self, locators):

        element = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable((By.XPATH, locators))
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        WebDriverWait(self.driver, 100).until(
            expected_conditions.visibility_of_element_located((By.XPATH, locators)))

        element.click()

    def get_accordion_panel(self, locators):

        return self.driver.find_element(By.XPATH, locators).text

    def click_order_button_top(self):

        WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable((By.XPATH, ORDER_BUTTON_TOP))).click()

    def click_order_button_buttom(self):

        element = WebDriverWait(self.driver, 100).until(
            EC.element_to_be_clickable((By.XPATH, ORDER_BUTTON_BOTTOM)))

        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        element.click()

