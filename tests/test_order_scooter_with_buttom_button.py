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

    def test_order_with_buttom_button(self):
        home_page = Homepagescooter(self.driver)
        home_page.wait_for_load_home_page()
        home_page.click_order_button_buttom()

        order_page = Orderpagescooter(self.driver)
        order_page.wait_for_load_order_page()
        order_page.set_name('Вика')
        order_page.set_last_name('Катина')
        order_page.set_address('Мурысева 18')
        order_page.set_metro('Черкизовская')
        order_page.set_phone_number('+79384756473')
        order_page.click_next_button()

        order_page.set_when_order('29.10.2024')
        order_page.set_how_long('двое суток')
        order_page.set_scooter_color_black()
        order_page.set_comment('Приезжайте побыстрее')
        order_page.click_order_button()
        order_page.click_order_confirmation()

        message_about_successful_order_creation = order_page.message_about_successful_order_creation()

        assert message_about_successful_order_creation.startswith("Заказ оформлен")
        order_page.click_watch_status_button()

        order_page.click_scooter_logo()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_to_be("https://qa-scooter.praktikum-services.ru/"))
        assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()