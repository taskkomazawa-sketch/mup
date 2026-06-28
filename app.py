from engine.layout.loader import LayoutLoader
from engine.layout.store_builder import StoreBuilder

loader = LayoutLoader(
    "data/layouts/minowa_uno_coordinate_map.xlsx"
)

cells = loader.load()

builder = StoreBuilder()

store = builder.build(
    "三ノ輪UNO",
    cells,
)

print(store.name)

seat640 = store.get_seat(640)

print(seat640)

print()

print(store.get_cell("R12"))

print()

promotion = store.seats_by_zone("Promotion")

print(f"Promotion Zone : {len(promotion)} seats")

for seat in promotion:
    print(seat.number)

from engine.layout.graph import CellGraph

graph = CellGraph(cells)

cell = graph.get("R12")

print(cell)
print("UP   :", graph.up(cell))
print("DOWN :", graph.down(cell))
print("LEFT :", graph.left(cell))
print("RIGHT:", graph.right(cell))