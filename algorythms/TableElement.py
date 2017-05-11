from enum import Enum


class TableElement():
    def __init__(self, locator):
        self.locator = locator

    def get_status(self):
        pass


class TableElementStatus(Enum):
    NULL = 0
    EMPTY = -1
    FULL = 1


