from enum import Enum


class TableElement():
    q = 2

    def __init__(self, table_locator=None, x=None, y=None):
        self.status = TableElementStatus.NULL

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = TableElementStatus.get_by_value(status)

    def check(self):
        self.click()
        self.status = TableElementStatus.get_by_value(self.wait_for_result())
        if self.status == TableElementStatus.EMPTY:
            return False
        if self.status == TableElementStatus.FULL:
            directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            self.kill(directions)
            return True

    def click(self):
        pass

    def wait_for_result(self):
        pass

    def kill(self, directions):
        for direction in directions:
            neighbor = self.get_neighbor(direction)
            if neighbor is not None:
                neighbor.click()
                if neighbor.get_status() == TableElementStatus.FULL:
                    self.kill(direction)
                if neighbor.get_status() == TableElementStatus.KILLED:
                    return

    def get_directions(self, direction):
        target_directions = []
        if direction[0]!=0:
            pass



    def get_neighbor(self, direction):
        return TableElement()


class TableElementStatus(Enum):
    NULL = 0
    EMPTY = -1
    FULL = 1
    KILLED = 2

    @staticmethod
    def get_by_value(val):
        return STATUS_DICTIONARY[val]


STATUS_DICTIONARY = {
    '0': TableElementStatus.NULL,
    '-1': TableElementStatus.EMPTY,
    '1': TableElementStatus.FULL,
    '2': TableElementStatus.KILLED
}
