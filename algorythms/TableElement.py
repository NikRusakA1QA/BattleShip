from enum import Enum

class TableElement():
    q = 2

    def __init__(self, locator=None):
        self.status = TableElementStatus.NULL

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = TableElementStatus.get_by_value(status)

    def check(self):
        self.status = TableElementStatus.FULL
        return False


class TableElementStatus(Enum):
    NULL = 0
    EMPTY = -1
    FULL = 1

    @staticmethod
    def get_by_value(val):
        return STATUS_DICTIONARY[val]


STATUS_DICTIONARY = {
    '0': TableElementStatus.NULL,
    '-1': TableElementStatus.EMPTY,
    '1': TableElementStatus.FULL
}


