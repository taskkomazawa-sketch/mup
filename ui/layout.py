import streamlit as st


def show_layout(store):

    st.divider()

    st.subheader("Layout")

    for seat in sorted(store.seats, key=lambda s: s.number):

        st.write(
            f"{seat.number}  ({seat.cell.id})"
        )