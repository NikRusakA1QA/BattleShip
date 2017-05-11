from algorythms.TableElement import TableElementStatus


class Figure():
    def __init__(self, heigh, width, grid):
        self.heigh = heigh
        self.width = width
        self.steps = min(self.heigh, self.width)
        self.grid = grid

    def get_figure(self, array, pointX, pointY):
        if pointX - self.width > 0 and pointY - self.heigh > 0:
            return array[pointX - self.width:pointX][pointY - self.heigh:pointY]

    def check_if_available(self, array, pointX, pointY):
        figure = self.get_figure(array, pointX, pointY)
        for rows in figure:
            for element in rows:
                if element.get_status() != TableElementStatus.NULL:
                    return False
        return figure is not None

    def find_value_in_grid(self, value):
        for row_index in range(len(self.grid)):
            for column_index in range(len(row_index)):
                if self.grid[row_index][column_index] == value: return (row_index, column_index)

    def fill(self, array, pointX, pointY):
        if self.check_if_available(array, pointX, pointY):
            self._fill(self.get_figure(array, pointX, pointY))

    def _fill(self, array):
        for i in range(1, self.steps):
            x, y = self.find_value_in_grid(i)
            if array[x][y].check():
                break


class Square4x4(Figure):
    grid = [[1, 0, 0, 0],
            [0, 2, 0, 0],
            [0, 0, 0, 3],
            [0, 0, 4, 0]]

    def __init__(self):
        super().__init__(4, 4, self.grid)


class Rectangle4x2(Figure):
    grid = [[1, 0],
            [0, 0],
            [0, 0],
            [0, 2]]

    def __init__(self):
        super().__init__(4, 2, self.grid)


class Rectangle2x4(Figure):
    grid = [[1, 0, 0, 0],
            [0, 0, 0, 2]]

    def __init__(self):
        super().__init__(2, 4, self.grid)


class Square3x3(Figure):
    grid = [[1, 0, 0],
            [0, 2, 0],
            [0, 0, 3]]

    def __init__(self):
        super().__init__(3, 3, self.grid)


class Rectangle3x2(Figure):
    grid = [[1, 0],
            [0, 0],
            [0, 2]]

    def __init__(self):
        super().__init__(3, 2, self.grid)


class Rectangle2x3(Figure):
    grid = [[1, 0, 0],
            [0, 0, 2]]

    def __init__(self):
        super().__init__(2, 3, self.grid)


class Rectangle2x2(Figure):
    grid = [[1, 0],
            [0, 2]]

    def __init__(self):
        super().__init__(2, 2, self.grid)


class Rectangle2x1(Figure):
    grid = [[1],
            [0]]

    def __init__(self):
        super().__init__(2, 1, self.grid)

class Rectangle1x2(Figure):
    grid = [[1, 0]]

    def __init__(self):
        super().__init__(1, 2, self.grid)

