from features.algorythms.table_element import TableElement


class Matrix():
    def __init__(self, table_locator, status_addition, x=10, y=10):
        self.height = x
        self.width = y
        self.table_locator = table_locator
        self.status_addition = status_addition
        self.content = []
        self.update()

    def update(self):
        for j in range(self.height):
            row = []
            for i in range(self.width):
                row.append(TableElement(self.table_locator, self.status_addition, j, i))
            self.content.append(row)

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
                success = figure.fill(self.content, x, y)
                if success: self.update()





