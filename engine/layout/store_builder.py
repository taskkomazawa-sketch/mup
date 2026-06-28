from models.seat import Seat
from models.store import Store

from engine.layout.zone_manager import ZoneManager


class StoreBuilder:

    def __init__(self):

        self.zone_manager = ZoneManager()

    def build(self, name, cells):

        seats = []

        for cell in cells:

            if isinstance(cell.value, int):

                seats.append(
                    Seat(
                        number=cell.value,
                        cell=cell,
                        zone=self.zone_manager.get_zone(cell.id),
                    )
                )

        return Store(
            name=name,
            cells=cells,
            seats=seats,
        )