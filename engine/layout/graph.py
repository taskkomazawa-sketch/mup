from models.cell import Cell


class CellGraph:

    def __init__(self, cells: list[Cell]):

        self.by_id = {}
        self.by_pos = {}

        for cell in cells:
            self.by_id[cell.id] = cell
            self.by_pos[(cell.row, cell.col)] = cell

    def get(self, cell_id: str):
        return self.by_id.get(cell_id)

    def get_by_pos(self, row: int, col: int):
        return self.by_pos.get((row, col))

    def up(self, cell: Cell):
        return self.get_by_pos(cell.row - 1, cell.col)

    def down(self, cell: Cell):
        return self.get_by_pos(cell.row + 1, cell.col)

    def left(self, cell: Cell):
        return self.get_by_pos(cell.row, cell.col - 1)

    def right(self, cell: Cell):
        return self.get_by_pos(cell.row, cell.col + 1)