from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import Homepagescooter
from pages.order_page import Orderpagescooter


class Testorder():

    driver = None

    @classmethod
    def setup_class(cls):

        cls.driver = webdriver.Firefox()
        cls.driver.get("https://qa-scooter.praktikum-services.ru/")

    def test_order_with_top_button(self):
        home_page = Homepagescooter(self.driver)
        home_page.wait_for_load_home_page()
        home_page.click_order_button_top()

        order_page = Orderpagescooter(self.driver)
        order_page.wait_for_load_order_page()
        order_page.set_name('Катя')
        order_page.set_last_name('Пупкина')
        order_page.set_address('Пушкина 18')
        order_page.set_metro('Сокольники')
        order_page.set_phone_number('+73487348347')
        order_page.click_next_button()

        order_page.set_when_order('20.10.2024')
        order_page.set_how_long('трое суток')
        order_page.set_scooter_color_gray()
        order_page.set_comment('Приезжайте побыстрее')
        order_page.click_order_button()
        order_page.click_order_confirmation()

        message_about_successful_order_creation = order_page.message_about_successful_order_creation()

        assert message_about_successful_order_creation.startswith("Заказ оформлен")
        order_page.click_watch_status_button()

        original_window = self.driver.current_window_handle
        order_page.click_yandex_logo()
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_to_be("https://dzen.ru/?yredirect=true"))
        assert self.driver.current_url == "https://dzen.ru/?yredirect=true"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
