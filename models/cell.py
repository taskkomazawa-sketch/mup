from dataclasses import dataclass


@dataclass(slots=True)
class Cell:
    id: str
    row: int
    col: int
    value: object | None = None

    def __repr__(self):
        return f"Cell({self.id}, value={self.value})"