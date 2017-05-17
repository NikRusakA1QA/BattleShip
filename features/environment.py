from features.algorythms.driver import BattleShipDriver


def after_feature(context, feature):
    BattleShipDriver.get_driver().quit()