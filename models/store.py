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

    def get_cell(self, cell_id: str) -> Cell | None:
        return self._cells.get(cell_id)

    def get_seat(self, seat_no: int) -> Seat | None:
        return self._seats.get(seat_no)

    def seats_by_zone(self, zone_name: str):
        return [
            seat
            for seat in self.seats
            if seat.zone.name == zone_name
        ]