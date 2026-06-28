import streamlit as st

from engine.layout.loader import LayoutLoader
from engine.layout.store_builder import StoreBuilder


st.set_page_config(
    page_title="MUP",
    page_icon="🎰",
    layout="wide",
)

st.title("🎰 MUP")
st.caption("Minowa UNO Prediction")


loader = LayoutLoader(
    "data/layouts/minowa_uno_coordinate_map.xlsx"
)

cells = loader.load()

builder = StoreBuilder()

store = builder.build(
    "三ノ輪UNO",
    cells,
)

promotion = store.seats_by_zone("Promotion")

c1, c2, c3 = st.columns(3)

c1.metric("Cells", len(store.cells))
c2.metric("Seats", len(store.seats))
c3.metric("Promotion", len(store.seats_by_zone("Promotion")))

st.divider()

rows = [
    {
        "Seat": seat.number,
        "Cell": seat.cell.id,
        "Zone": seat.zone.name,
    }
    for seat in sorted(store.seats, key=lambda s: s.number)
]

st.dataframe(
    rows,
    use_container_width=True,
    hide_index=True,
)