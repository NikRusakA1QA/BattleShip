from enum import Enum


class ShipTypes(Enum):
    SIZE_4 = "4"
    SIZE_3 = "3"
    SIZE_2 = "2"
    SIZE_1 = "1"


class Ships():
    def __init__(self):
        self.ships = [ShipTypes.SIZE_4,
                      ShipTypes.SIZE_3, ShipTypes.SIZE_3,
                      ShipTypes.SIZE_2, ShipTypes.SIZE_2, ShipTypes.SIZE_2,
                      ShipTypes.SIZE_1, ShipTypes.SIZE_1, ShipTypes.SIZE_1, ShipTypes.SIZE_1]

    def check(self):
        return self.ships is []

    def check_size(self, ship_type):
        return ship_type in self.ships

    def destroy(self, ship_type):
        self.ships.remove(ship_type)
        return self.check()
