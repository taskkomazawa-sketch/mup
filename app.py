import streamlit as st

from engine.layout.loader import LayoutLoader
from engine.layout.store_builder import StoreBuilder
from ui.dashboard import show_dashboard

st.set_page_config(
    page_title="MUP",
    page_icon="🎰",
    layout="wide",
)

if "store" not in st.session_state:
    loader = LayoutLoader("data/layouts/minowa_uno_coordinate_map.xlsx")
    cells = loader.load()

    builder = StoreBuilder()
    st.session_state.store = builder.build(
        "三ノ輪UNO",
        cells,
    )

store = st.session_state.store

show_dashboard(store)