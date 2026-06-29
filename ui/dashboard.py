import streamlit as st

from ui.layout import show_layout


def show_dashboard(store):
    st.title("🎰 MUP")
    st.caption("Minowa UNO Digital Twin")

    c1, c2, c3 = st.columns(3)

    c1.metric("Cells", len(store.cells))
    c2.metric("Seats", len(store.seats))
    c3.metric("Promotion", len(store.seats_by_zone("Promotion")))

    left, right = st.columns([3, 1])

    with left:
        show_layout(store)

    with right:
        seat_numbers = sorted(
            seat.number
            for seat in store.seats
        )

        selected = st.selectbox(
            "Seat",
            seat_numbers,
            key="seat_selector",
        )

        seat = store.get_seat(selected)

        st.subheader("Seat Detail")
        st.write(f"**Seat** : {seat.number}")
        st.write(f"**Zone** : {seat.zone.name}")
        st.write(f"**Cell** : {seat.cell.id}")
        st.write(f"**Row** : {seat.cell.row}")
        st.write(f"**Column** : {seat.cell.col}")