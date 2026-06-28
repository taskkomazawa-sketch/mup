import streamlit as st
from ui.layout import show_layout

def show_dashboard(store):
    st.title("🎰 MUP")
    st.caption("Minowa UNO Digital Twin")

    col1, col2, col3 = st.columns(3)

    col1.metric("Cells", len(store.cells))
    col2.metric("Seats", len(store.seats))
    col3.metric(
        "Promotion",
        len(store.seats_by_zone("Promotion"))
    )
    show_layout(store)
    # ここに今のdataframe表示も移す