from dataclasses import dataclass, field

from models.cell import Cell
from models.zone import Zone
from models.seat_state import SeatState


@dataclass
class Seat:
    number: int
    cell: Cell
    zone: Zone
    state: SeatState = field(default_factory=SeatState)