import streamlit as st

from engine.data.csv_loader import load_csv
from ui.layout import show_layout


def show_dashboard(store):
    st.title("🎰 MUP")
    st.caption("Minowa UNO Digital Twin")

    uploaded = st.file_uploader(
        "営業データ(CSV)",
        type="csv",
    )

    if uploaded:
        rows = load_csv(uploaded)
        store.apply_csv(rows)

    c1, c2, c3 = st.columns(3)

    c1.metric("Cells", len(store.cells))
    c2.metric("Seats", len(store.seats))
    c3.metric("Promotion", len(store.seats_by_zone("Promotion")))

    left, right = st.columns([3, 1])

    seat_numbers = sorted(seat.number for seat in store.seats)

    selected = right.selectbox(
        "Seat",
        seat_numbers,
        key="seat_selector",
    )

    with left:
        show_layout(store, selected_seat=selected)

    with right:
        seat = store.get_seat(selected)

        st.subheader("Seat Detail")
        st.write(f"**Seat** : {seat.number}")
        st.write(f"**Zone** : {seat.zone.name}")
        st.write(f"**Cell** : {seat.cell.id}")
        st.write(f"**Row** : {seat.cell.row}")
        st.write(f"**Column** : {seat.cell.col}")
        st.write(f"**Games** : {seat.state.games}")
        st.write(f"**Diff** : {seat.state.diff:+}")
        st.divider()
        st.subheader("Neighbors")

        for direction, icon in [
            ("up", "⬆️"),
            ("down", "⬇️"),
            ("left", "⬅️"),
            ("right", "➡️"),
        ]:
            neighbor = store.get_neighbor(seat, direction)

            st.write(
                icon,
                neighbor.number if neighbor else "通路",
            )