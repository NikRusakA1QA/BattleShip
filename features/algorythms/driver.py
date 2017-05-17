
from numpy import random
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from features.algorythms.config import Config
from features.algorythms.custom_exceptions import GameWin, UnexpectedGameFinish


class BattleShipDriver:
    driver = None

    @staticmethod
    def get_driver():
        if BattleShipDriver.driver is None:
            BattleShipDriver.driver = Firefox()
        return BattleShipDriver.driver

    @staticmethod
    def open_battleship_main_page():
        driver = BattleShipDriver.get_driver()
        driver.start_client()
        driver.get(Config.get_config().battleship_url)

    @staticmethod
    def assert_main_title():
        WebDriverWait(BattleShipDriver.get_driver(), Config.get_config().timeout).until_not(BattleShipDriver.check_element_text(Config.get_config().main_title_locator, Config.get_config().main_title))

    @staticmethod
    def place_ships():
        for i in range(random.randint(1, 15)):
            BattleShipDriver.click_element(Config.get_config().place_ships_button_locator)

    @staticmethod
    def find_element(locator):
        return WebDriverWait(BattleShipDriver.get_driver(), Config.get_config().timeout).until(
        expected_conditions.presence_of_element_located((By.XPATH, locator))
    )

    @staticmethod
    def get_element_text(locator):
        return BattleShipDriver.get_driver().find_element_by_xpath(locator).text


    @staticmethod
    def click_start():
        return BattleShipDriver.click_element(Config.get_config().start_button)

    @staticmethod
    def wait_for_opponent():
        WebDriverWait(BattleShipDriver.get_driver(), Config.get_config().timeout).until_not(
            BattleShipDriver.game_started(Config.get_config().notification_method_locator, Config.get_config().wait_start_game_opponent_turn_message, Config.get_config().wait_start_game_your_turn_message))

    @staticmethod
    def click_element(locator):
        WebDriverWait(BattleShipDriver.get_driver(), Config.get_config().timeout).until(expected_conditions.element_to_be_clickable((By.XPATH, locator))).click()

    @staticmethod
    def wait_for_your_turn():
        attempts = 0
        while attempts<Config.get_config().max_attempts:
            attempts+=1
            try:
                WebDriverWait(BattleShipDriver.get_driver(), Config.get_config().timeout).until(BattleShipDriver.wait_for_element_status(Config.get_config().opponent_field_locator, Config.get_config().wait_status))
                return
            except:
                BattleShipDriver.check_message()

    @staticmethod
    def check_message():
        notification_element = BattleShipDriver.get_driver().find_element_by_xpath(
            Config.get_config().notification_method_locator)
        text = notification_element.text
        if not text in (Config.get_config().your_turn_message, Config.get_config().wait_your_turn_message):
            if text == Config.get_config().win_game_string:
                raise GameWin(text)
            else:
                raise UnexpectedGameFinish(text)

    @staticmethod
    def get_message_from_notification():
        notification_element = BattleShipDriver.get_driver().find_element_by_xpath(Config.get_config().notification_method_locator)
        return notification_element.text

    @staticmethod
    def wait_for_status_update(status_locator, null_status):
        try:
            WebDriverWait(BattleShipDriver.get_driver(), Config.get_config().timeout).until(BattleShipDriver.wait_for_element_status(status_locator, null_status))
        except:
            BattleShipDriver.check_message()

    @staticmethod
    def click_table_element(locator):
        BattleShipDriver.click_element(locator)

    class check_element_text(object):
        def __init__(self, locator, text):
            self.locator = locator
            self.text = text

        def __call__(self, driver):
            return BattleShipDriver.find_element(self.locator).text == self.text

    class game_started(object):
        def __init__(self, locator, text_your_turn, text_opponent_turn):
            self.locator = locator
            self.text_your_turn = text_your_turn
            self.text_opponent_turn = text_opponent_turn

        def __call__(self, driver):
            return BattleShipDriver.get_element_text(self.locator) in (self.text_your_turn, self.text_opponent_turn)

    class wait_for_element_status():
        def __init__(self, status_locator, null_status):
            self.status_locator = status_locator
            self.null_status = null_status

        def __call__(self, driver):
            element = BattleShipDriver.find_element(self.status_locator)
            class_string = element.get_attribute("class")
            return class_string.find(self.null_status) is -1
