from enum import Enum

import numpy

from features.algorythms.config import Config
from features.algorythms.driver import BattleShipDriver as Driver
from features.algorythms.ships import ShipTypes, Ships


class TableElement():
    def __init__(self, table_locator, status_locator_addition, x, y):
        self.table_locator = table_locator
        self.x = x
        self.y = y
        self.locator = table_locator % (x, y)
        self.status_addition = status_locator_addition
        self.status_locator = self.locator + status_locator_addition
        self.update_status()

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = TableElementStatus.get_by_value(status)

    def check(self):
        self.click()
        if self.status == TableElementStatus.EMPTY:
            return False
        if self.status == TableElementStatus.FULL:
            directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            self.kill(directions, 1)
            return True

    def click(self):
        Driver.wait_for_your_turn()
        self.update_status()
        if self.status is TableElementStatus.NULL:
            Driver.click_table_element(self.locator)
            self.wait_for_result()
        self.update_status()

    def wait_for_result(self):
        null_status = TableElementStatus.get_key(TableElementStatus.NULL)
        Driver.wait_for_status_update(self.status_locator, null_status)
        Driver.wait_for_your_turn()

    def update_status(self):
        element = Driver.find_element(self.status_locator)
        elem_status = element.get_attribute("class")
        self.set_status(elem_status)

    def kill(self, directions, length):
        for direction in directions:
            neighbor = self.get_neighbor(direction)
            if neighbor is not None:
                neighbor.click()
                if neighbor.get_status() == TableElementStatus.FULL:
                    self.kill(self.get_directions(direction), length + 1)
                if neighbor.get_status() == TableElementStatus.KILLED:
                    ship_type = ShipTypes.get_type_by_size(length)
                    Ships.destroy(ship_type)
                    return

    def get_directions(self, direction):
        target_directions = []
        self.add_direction(direction[0], target_directions, 0)
        self.add_direction(direction[1], target_directions, 1)
        return target_directions

    def add_direction(self, direction_val, target_directions, index):
        if direction_val != 0:
            new_direction_same = direction_val + numpy.sign(direction_val)
            new_direction_opposite = (-1) * numpy.sign(direction_val)
            self.set_direction(target_directions, new_direction_same, index)
            self.set_direction(target_directions, new_direction_opposite, index)

    def set_direction(self, target, val, index):
        if index == 0:
            target.append((val, 0))
        else:
            target.append((0, val))

    def get_neighbor(self, direction):
        if (0 <= self.x + direction[0] < Config.get_config().width
            and 0 <= self.y + direction[1] < Config.get_config().heigh):
            return TableElement(self.table_locator, self.status_addition, self.x + direction[0], self.y + direction[1])


class TableElementStatus(Enum):
    NULL = 0
    EMPTY = -1
    FULL = 1
    KILLED = 2

    @staticmethod
    def get_by_value(val):
        values = []
        for key, value in STATUS_DICTIONARY.items():
            if val.find(key) != -1:
                values.append(value)
        if (TableElementStatus.FULL in values and TableElementStatus.KILLED in values):
            return TableElementStatus.KILLED
        return values[0]

    @staticmethod
    def get_key(val):
        for key, value in STATUS_DICTIONARY.items():
            if value == val:
                return key


STATUS_DICTIONARY = {
    'battlefield-cell battlefield-cell__empty': TableElementStatus.NULL,
    'battlefield-cell battlefield-cell__miss': TableElementStatus.EMPTY,
    'battlefield-cell__hit': TableElementStatus.FULL,
    'battlefield-cell__hit battlefield-cell__done': TableElementStatus.KILLED
}
