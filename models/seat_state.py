from dataclasses import dataclass


@dataclass
class SeatState:
    games: int = 0
    diff: int = 0
    setting: int | None = None