from enum import Enum


class ShipTypes(Enum):
    SIZE_4 = "4"
    SIZE_3 = "3"
    SIZE_2 = "2"
    SIZE_1 = "1"

    @staticmethod
    def get_type_by_size(val):
        return SHIPS_DICTIONARY[val]

SHIPS_DICTIONARY = {
    1:ShipTypes.SIZE_1,
    2:ShipTypes.SIZE_2,
    3:ShipTypes.SIZE_3,
    4:ShipTypes.SIZE_4
}

class Ships():
    ships = [ShipTypes.SIZE_4,
                      ShipTypes.SIZE_3, ShipTypes.SIZE_3,
                      ShipTypes.SIZE_2, ShipTypes.SIZE_2, ShipTypes.SIZE_2,
                      ShipTypes.SIZE_1, ShipTypes.SIZE_1, ShipTypes.SIZE_1, ShipTypes.SIZE_1]

    @staticmethod
    def check():
        return Ships.ships is []

    @staticmethod
    def check_size(ship_type):
        return ship_type in Ships.ships

    @staticmethod
    def destroy(ship_type):
        if Ships.check_size(ship_type):
            Ships.ships.remove(ship_type)
        return Ships.check()
