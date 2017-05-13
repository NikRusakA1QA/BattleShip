from algorythms.Matrix import Matrix


class Table():
    def __init__(self, table_locator="locator", heigh=10, width=10):
        self.table_locator = table_locator
        self.matrix = Matrix()
        self.update_matrix()

    def update_matrix(self):
        matrix = []
        with open("field_visible") as f:
            for line in f.readlines():
                elements = line.split(" ")
                matrix.append(elements)
        self.matrix.update(matrix)

    def update_table(self):
        with open("field_visible") as f:
            for row in self.matrix.get_content_statuses_as_array():
                f.write(" ".join(row) + "\n")

    def print(self):
        for row in self.matrix.get_content_statuses_as_array():
            print(" ".join(row))

    def fill_figure_in_matrix(self, figure):
        self.matrix.find_figure(figure)

