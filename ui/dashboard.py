import streamlit as st

from ui.layout import show_layout


def show_dashboard(store):
    st.title("🎰 MUP")
    st.caption("Minowa UNO Digital Twin")

    c1, c2, c3 = st.columns(3)

    c1.metric("Cells", len(store.cells))
    c2.metric("Seats", len(store.seats))
    c3.metric("Promotion", len(store.seats_by_zone("Promotion")))

    show_layout(store)