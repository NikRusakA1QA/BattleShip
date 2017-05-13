class Table():
    def __init__(self, table_locator="locator", heigh=10, width=10):
        self.table_locator = table_locator

    def get_matrix(self):
        matrix = []
        with open("field_visible") as f:
            for line in f.readlines():
                elements = line.split(" ")
