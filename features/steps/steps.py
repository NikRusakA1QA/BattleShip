from behave import given
from behave import then

from features.algorythms.config import Config
from features.algorythms.custom_exceptions import GameWin, UnexpectedGameFinish
from features.algorythms.driver import BattleShipDriver
from features.algorythms.table import Table


@given('I open battleship main page')
def open_battleship_main_page(context):
    BattleShipDriver.open_battleship_main_page()


@then('I should see main title')
def assert_main_title(context):
    BattleShipDriver.assert_main_title()


@given('I place ships randomly')
def place_ships(context):
    BattleShipDriver.place_ships()


@given('I click start')
def click_start(context):
    BattleShipDriver.click_start()


@given('I wait for opponent')
def wait_for_opponent(context):
    BattleShipDriver.wait_for_opponent()
    context.battle_table = Table(Config.get_config().table_locator, Config.get_config().status_addition)


@then('I use algorythm')
def fill_all_possible_figures(context):
    try:
        context.battle_table.fill_all_4_size_figures()
        context.battle_table.fill_all_3_size_figures()
        context.battle_table.fill_all_2_size_figures()
        context.battle_table.fill_all_1_size_figures()
        context.str = BattleShipDriver.get_message_from_notification()
    except GameWin as win:
        context.str = win.str
    except UnexpectedGameFinish as finish:
        context.str = finish.str


@then('I should win')
def check_if_win(context):
    assert context.str == Config.get_config().win_game_string, context.str
