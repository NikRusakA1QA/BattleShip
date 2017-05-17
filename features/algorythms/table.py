from features.algorythms import figures
from features.algorythms.matrix import Matrix


class Table():
    def __init__(self, table_locator, status_addition, heigh=10, width=10):
        self.matrix = Matrix(table_locator, status_addition)

    def fill_figure_in_matrix(self, figure):
        self.matrix.find_figure(figure)

    def fill_all_figures(self, figures):
        for figure in figures:
            self.fill_figure_in_matrix(figure)

    def fill_all_4_size_figures(self):
        figures_to_fill = [figures.Square4x4(), figures.Rectangle2x4(), figures.Rectangle4x2(), figures.Rectangle1x4(),
                           figures.Rectangle4x1()]
        self.fill_all_figures(figures_to_fill)

    def fill_all_3_size_figures(self):
        figures_to_fill = [figures.Square3x3(), figures.Rectangle2x3(), figures.Rectangle3x2()]
        self.fill_all_figures(figures_to_fill)

    def fill_all_2_size_figures(self):
        figures_to_fill = [figures.Rectangle2x2(), figures.Rectangle2x1(), figures.Rectangle1x2()]
        self.fill_all_figures(figures_to_fill)

    def fill_all_1_size_figures(self):
        figures_to_fill = [figures.Rectangle1x1()]
        self.fill_all_figures(figures_to_fill)
