import json
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config():
    config = None
    def __init__(self):
        with open(BASE_DIR+"/config.json") as file:
            config_json = json.load(file)
        locators = config_json["locators"]
        config = config_json["config"]
        asserts = config_json["asserts"]
        self.table_locator = locators["table_locator"]
        self.status_addition = locators["status_addition"]
        self.opponent_field_locator = locators["opponent_field_locator"]
        self.notification_method_locator = locators["notification_method_locator"]
        self.main_title_locator = locators["main_title_locator"]
        self.place_ships_button_locator = locators["place_ships_button_locator"]
        self.start_button = locators["start_button"]
        self.timeout = config["timeout"]
        self.max_attempts = config["max_attempts"]
        self.battleship_url = config["battleship_url"]
        self.heigh = config["heigh"]
        self.width = config["width"]
        self.win_game_string = asserts["win_game_string"]
        self.wait_status = asserts["wait_status"]
        self.wait_your_turn_message = asserts["wait_your_turn_message"]
        self.your_turn_message = asserts["your_turn_message"]
        self.wait_start_game_your_turn_message = asserts["wait_start_game_your_turn_message"]
        self.wait_start_game_opponent_turn_message = asserts["wait_start_game_opponent_turn_message"]
        self.wait_for_opponent_message = asserts["wait_for_opponent_message"]
        self.main_title = asserts["main_title"]

    @staticmethod
    def get_config():
        if Config.config is None:
            Config.config = Config()
        return Config.config



