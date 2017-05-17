from features.algorythms.config import Config
from features.algorythms.ships import ShipTypes, Ships
from features.algorythms.table_element import TableElementStatus


class Figure():
    def __init__(self, heigh, width, grid, target_ship):
        self.heigh = heigh
        self.width = width
        self.steps = min(self.heigh, self.width)
        self.grid = grid
        self.target_ship = target_ship

    def get_figure(self, array, pointX, pointY):
        if self.width == 1 and self.heigh == 1:
            return [[array[pointX][pointY]]]
        if 0<=pointX + self.width <= Config.get_config().width and 0<=pointY + self.heigh <= Config.get_config().heigh:
            return self._get_dd_array_part(array, (pointX, pointX + self.width), (pointY, pointY + self.heigh))

    def _get_dd_array_part(self, array, rows, columns):
        part_rows = array[rows[0]:rows[1]]
        part = []
        for line in part_rows:
            line = line[columns[0]:columns[1]]
            part.append(line)
        return part

    def check_if_available(self, array, pointX, pointY):
        figure = self.get_figure(array, pointX, pointY)
        if figure is None:
            return None
        for rows in figure:
            for element in rows:
                if element.get_status() != TableElementStatus.NULL:
                    return False
        return True

    def find_value_in_grid(self, value):
        for row_index in range(self.heigh):
            for column_index in range(self.width):
                if self.grid[row_index][column_index] == value:
                    return row_index, column_index

    def fill(self, array, point_x, point_y):
        if Ships.check_size(self.target_ship) and self.check_if_available(array, point_x, point_y):
            self._fill(self.get_figure(array, point_x, point_y))
            return True
        return False

    def _fill(self, array):
        if len(array)==0:
            return
        for i in range(1, self.steps + 1):
            x, y = self.find_value_in_grid(i)
            if array[y][x].check():
                break


class Square4x4(Figure):
    grid = [[1, 0, 0, 0],
            [0, 2, 0, 0],
            [0, 0, 0, 3],
            [0, 0, 4, 0]]

    target_ship = ShipTypes.SIZE_4

    def __init__(self):
        super().__init__(4, 4, self.grid, self.target_ship)


class Rectangle4x2(Figure):
    grid = [[1, 0],
            [0, 0],
            [0, 0],
            [0, 2]]

    target_ship = ShipTypes.SIZE_4

    def __init__(self):
        super().__init__(4, 2, self.grid, self.target_ship)


class Rectangle2x4(Figure):
    grid = [[1, 0, 0, 0],
            [0, 0, 0, 2]]

    target_ship = ShipTypes.SIZE_4

    def __init__(self):
        super().__init__(2, 4, self.grid, self.target_ship)

class Rectangle1x4(Figure):
    grid = [[1, 0, 0, 0]]

    target_ship = ShipTypes.SIZE_4

    def __init__(self):
        super().__init__(1, 4, self.grid, self.target_ship)

class Rectangle4x1(Figure):
    grid = [[1],
            [0],
            [0],
            [0]]

    target_ship = ShipTypes.SIZE_4

    def __init__(self):
        super().__init__(4, 1, self.grid, self.target_ship)


class Square3x3(Figure):
    grid = [[1, 0, 0],
            [0, 2, 0],
            [0, 0, 3]]

    target_ship = ShipTypes.SIZE_3


    def __init__(self):
        super().__init__(3, 3, self.grid, self.target_ship)


class Rectangle3x2(Figure):
    grid = [[1, 0],
            [0, 0],
            [0, 2]]

    target_ship = ShipTypes.SIZE_3


    def __init__(self):
        super().__init__(3, 2, self.grid, self.target_ship)


class Rectangle2x3(Figure):
    grid = [[1, 0, 0],
            [0, 0, 2]]

    target_ship = ShipTypes.SIZE_3


    def __init__(self):
        super().__init__(2, 3, self.grid, self.target_ship)


class Rectangle2x2(Figure):
    grid = [[1, 0],
            [0, 2]]

    target_ship = ShipTypes.SIZE_2

    def __init__(self):
        super().__init__(2, 2, self.grid, self.target_ship)


class Rectangle2x1(Figure):
    grid = [[1],
            [0]]

    target_ship = ShipTypes.SIZE_2


    def __init__(self):
        super().__init__(2, 1, self.grid, self.target_ship)


class Rectangle1x2(Figure):
    grid = [[1, 0]]

    target_ship = ShipTypes.SIZE_2


    def __init__(self):
        super().__init__(1, 2, self.grid, self.target_ship)



class Rectangle1x1(Figure):
    grid = [[1]]

    target_ship = ShipTypes.SIZE_1

    def __init__(self):
        super().__init__(1, 1, self.grid, self.target_ship)

