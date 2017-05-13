from algorythms.TableElement import TableElement


class Matrix():
    def __init__(self, x=10, y=10):
        self.height = x
        self.width = y
        self.content = []
        for j in range(x):
            row = []
            for i in range(y):
                row.append(TableElement())
            self.content.append(row)

    def update(self, array):
        for row_source, row_target in zip(array, self.content):
            for element_source, element_target in zip(row_source, row_target):
                element_target.set_status(element_source.replace("\n",""))

    def get_content_statuses_as_array(self):
        array = []
        for row in self.content:
            new_row = []
            for element in row:
                new_row.append(str(element.get_status().value))
            array.append(new_row)
        return array

    def find_figure(self, figure):
        for x in range(self.height):
            for y in range(self.width):
                figure.fill(self.content, x, y)





