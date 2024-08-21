from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.home_page__locators import ORDER_NAME, ORDER_LAST_NAME, ORDER_ADDRESS, ORDER_PHONE_NUMBER, ORDER_METRO, \
    ORDER_NEXT_BUTTON, ORDER_WHEN, ORDER_HOW_LONG, ORDER_COMMENT, ORDER_COMPLETE, SCOOTER_COLOR_BLACK, \
    SCOOTER_COLOR_GRAY, ORDER_CONFIRMATION_BUTTON, MESSAGE_ABOUT_SUCCESSFUL_ORDER_CREATION, WATCH_STATUS_BUTTON, \
    YANDEX_LOGO, SCOOTER_LOGO


class Orderpagescooter:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_order_page(self):

        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH ,ORDER_NEXT_BUTTON)))
    def set_name(self, name):
        self.driver.find_element(By.XPATH , ORDER_NAME).send_keys(name)

    def set_last_name(self, last_name):
        self.driver.find_element(By.XPATH ,ORDER_LAST_NAME).send_keys(last_name)

    def set_address(self, address):
        self.driver.find_element(By.XPATH ,ORDER_ADDRESS).send_keys(address)

    def set_phone_number(self, phone_number):
        self.driver.find_element(By.XPATH ,ORDER_PHONE_NUMBER).send_keys(phone_number)

    def set_metro(self, metro):
        self.driver.find_element(By.XPATH, ORDER_METRO).click()
        self.driver.find_element(By.XPATH, f"//button[starts-with(@class, 'Order_SelectOption')]/div[text()='{metro}']").click()

    def click_next_button(self):
        self.driver.find_element(By.XPATH ,ORDER_NEXT_BUTTON).click()

    def set_when_order(self, when_order):

        element = self.driver.find_element(By.XPATH ,ORDER_WHEN)
        element.send_keys(when_order)
        element.send_keys(Keys.ENTER)


    def set_how_long(self, how_long):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, ORDER_HOW_LONG)))
        element.click()


        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@class='Dropdown-option'][text()='{how_long}']")))
        element.click()


    def set_scooter_color_black(self):
        self.driver.find_element(By.CSS_SELECTOR , SCOOTER_COLOR_BLACK).click()

    def set_scooter_color_gray(self):
        self.driver.find_element(By.CSS_SELECTOR, SCOOTER_COLOR_GRAY).click()

    def set_comment(self, comment):
        self.driver.find_element(By.XPATH ,ORDER_COMMENT).send_keys(comment)

    def click_order_button(self):
        self.driver.find_element(By.XPATH ,ORDER_COMPLETE).click()

    def click_order_confirmation(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ORDER_CONFIRMATION_BUTTON))).click()


    def message_about_successful_order_creation(self):

        return self.driver.find_element(By.XPATH, MESSAGE_ABOUT_SUCCESSFUL_ORDER_CREATION).text

    def click_watch_status_button(self):
        self.driver.find_element(By.XPATH, WATCH_STATUS_BUTTON).click()

    def click_yandex_logo(self):

        self.driver.find_element(By.XPATH, YANDEX_LOGO).click()

    def click_scooter_logo(self):
        self.driver.find_element(By.XPATH, SCOOTER_LOGO).click()




