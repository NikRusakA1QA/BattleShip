from enum import Enum


class TableElement():
    q=2
    def __init__(self, locator):
        self.locator = locator
        self.status = TableElementStatus.NULL

    def get_status(self):
        return self.status

    def check(self):
        self.status = TableElement.q
        TableElement.q+=1


class TableElementStatus(Enum):
    NULL = 0
    EMPTY = -1
    FULL = 1


