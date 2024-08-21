from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.home_page__locators import ACCORDION_ITEM_HOW_PAY, ACCORDION_ITEM_FEW_SCOOTER, \
    ACCORDION_PANEL_FEW_SCOOTER, ACCORDION_PANEL_HOW_PAY, ACCORDION_ITEM_RENT_TIME, ACCORDION_PANEL_RENT_TIME, \
    ACCORDION_ITEM_RENT_FOR_TODAY, ACCORDION_PANEL_RENT_FOR_TODAY, ACCORDION_ITEM_RENEW_OR_RETURN_EARLIER, \
    ACCORDION_PANEL_RENEW_OR_RETURN_EARLIER, ACCORDION_ITEM_CHARGER, ACCORDION_PANEL_CHARGER, \
    ACCORDION_ITEM_DECLINE_ORDER, ACCORDION_PANEL_DECLINE_ORDER, ACCORDION_ITEM_LIVE_OUTSIDE_OF_MKAD, \
    ACCORDION_PANEL_LIVE_OUTSIDE_OF_MKAD
from pages.home_page import Homepagescooter


class Testquestions():

    driver = None

    @classmethod
    def setup_class(cls):

        cls.driver = webdriver.Firefox()
        cls.driver.get("https://qa-scooter.praktikum-services.ru/")


    def test_question_how_pay(self):

        home_page = Homepagescooter(self.driver)
        home_page.wait_for_load_home_page()
        home_page.click_accordion_item(ACCORDION_ITEM_HOW_PAY)
        assert home_page.get_accordion_panel(ACCORDION_PANEL_HOW_PAY) == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    def test_question_few_scooter(self):

        home_page = Homepagescooter(self.driver)
        home_page.wait_for_load_home_page()
        home_page.click_accordion_item(ACCORDION_ITEM_FEW_SCOOTER)
        assert home_page.get_accordion_panel(ACCORDION_PANEL_FEW_SCOOTER) == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."

    def test_question_rent_time(self):
        home_page = Homepagescooter(self.driver)
        home_page.wait_for_load_home_page()
        home_page.click_accordion_item(ACCORDION_ITEM_RENT_TIME)
        assert home_page.get_accordion_panel(ACCORDION_PANEL_RENT_TIME) == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

    def test_question_rent_for_today(self):
        home_page = Homepagescooter(self.driver)
        home_page.wait_for_load_home_page()
        home_page.click_accordion_item(ACCORDION_ITEM_RENT_FOR_TODAY)
        assert home_page.get_accordion_panel(ACCORDION_PANEL_RENT_FOR_TODAY) == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    def test_question_renew_or_return_earlier(self):
        home_page = Homepagescooter(self.driver)
        home_page.wait_for_load_home_page()
        home_page.click_accordion_item(ACCORDION_ITEM_RENEW_OR_RETURN_EARLIER)
        assert home_page.get_accordion_panel(ACCORDION_PANEL_RENEW_OR_RETURN_EARLIER) == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."

    def test_question_charger(self):
        home_page = Homepagescooter(self.driver)
        home_page.wait_for_load_home_page()
        home_page.click_accordion_item(ACCORDION_ITEM_CHARGER)
        assert home_page.get_accordion_panel(ACCORDION_PANEL_CHARGER) == "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."

    def test_question_decline_order(self):
        home_page = Homepagescooter(self.driver)
        home_page.wait_for_load_home_page()
        home_page.click_accordion_item(ACCORDION_ITEM_DECLINE_ORDER)
        assert home_page.get_accordion_panel(ACCORDION_PANEL_DECLINE_ORDER) == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."

    def test_question_live_outside_of_mkad(self):
        home_page = Homepagescooter(self.driver)
        home_page.wait_for_load_home_page()
        home_page.click_accordion_item(ACCORDION_ITEM_LIVE_OUTSIDE_OF_MKAD)
        assert home_page.get_accordion_panel(ACCORDION_PANEL_LIVE_OUTSIDE_OF_MKAD) == "Да, обязательно. Всем самокатов! И Москве, и Московской области."



    @classmethod
    def teardown_class(cls):

        cls.driver.quit()



