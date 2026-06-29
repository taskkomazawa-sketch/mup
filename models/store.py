from dataclasses import dataclass

from models.cell import Cell
from models.seat import Seat


@dataclass
class Store:
    name: str
    cells: list[Cell]
    seats: list[Seat]

    def __post_init__(self):
        self._cells = {c.id: c for c in self.cells}
        self._seats = {s.number: s for s in self.seats}
        self._cell_map = {
            (cell.row, cell.col): cell
            for cell in self.cells
        }
        self._seat_by_cell = {
            seat.cell.id: seat
            for seat in self.seats
        }        

    def get_cell(self, cell_id: str) -> Cell | None:
        return self._cells.get(cell_id)
    
    def get_cell_by_position(self, row: int, col: int):
        return self._cell_map.get((row, col))

    def get_seat(self, seat_no: int) -> Seat | None:
        return self._seats.get(seat_no)

    def seats_by_zone(self, zone_name: str):
        return [
            seat
            for seat in self.seats
            if seat.zone.name == zone_name
        ]
    def get_neighbor(self, seat: Seat, direction: str) -> Seat | None:
        offsets = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
        }

        dr, dc = offsets[direction]

        row = seat.cell.row + dr
        col = seat.cell.col + dc

        cell = self.get_cell_by_position(row, col)

        if cell is None:
            return None

        return self.find_seat_by_cell(cell)

    def find_seat_by_cell(self, cell: Cell) -> Seat | None:
        return self._seat_by_cell.get(cell.id)

    def apply_csv(self, rows):
        for row in rows:
            seat = self.get_seat(int(row["seat"]))

            if seat is None:
                continue

            seat.state.games = int(row["games"])
            seat.state.diff = int(row["diff"])
