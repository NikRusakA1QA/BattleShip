from algorythms import figures
from algorythms.Ships import Ships
from algorythms.Table import Table

table = Table()

table.fill_figure_in_matrix(figures.Square4x4())
table.fill_figure_in_matrix(figures.Rectangle2x4())
table.fill_figure_in_matrix(figures.Rectangle4x2())
table.fill_figure_in_matrix(figures.Rectangle1x4())
table.fill_figure_in_matrix(figures.Rectangle4x1())
table.print()

