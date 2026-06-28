from dataclasses import dataclass

from models.cell import Cell
from models.zone import Zone


@dataclass
class Seat:
    number: int
    cell: Cell
    zone: Zone