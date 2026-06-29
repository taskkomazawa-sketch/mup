import html

import streamlit as st


def show_layout(store, selected_seat=None):
    st.divider()
    st.subheader("Layout")

    rows = sorted({seat.cell.row for seat in store.seats})
    cols = sorted({seat.cell.col for seat in store.seats})

    seat_by_position = {
        (seat.cell.row, seat.cell.col): seat
        for seat in store.seats
    }

    table = """
    <style>
    .hall-wrap {
        overflow-x: auto;
        padding: 8px;
        background: #fafafa;
        border: 1px solid #ddd;
    }
    table.hall {
        border-collapse: collapse;
        table-layout: fixed;
    }
    table.hall td {
        width: 48px;
        min-width: 48px;
        height: 30px;
        border: 1px solid #ddd;
        text-align: center;
        vertical-align: middle;
        font-size: 11px;
        white-space: nowrap;
    }
    td.seat {
        background: #f3f4f6;
        font-weight: bold;
    }
    td.promotion {
        background: #b7f7c3;
        font-weight: bold;
    }
    td.newmachine {
        background: #b9d9ff;
        font-weight: bold;
    }
    td.blank {
        background: white;
        border-color: #f5f5f5;
    }
    td.selected {
        background: #fff176;
        font-weight: 900;
        border: 2px solid #f9a825;
    }
    td.heat4 {
    background: #2ecc71;
    font-weight: bold;
    }

    td.heat3 {
        background: #b7f7c3;
        font-weight: bold;
    }

    td.heat2 {
        background: #f3f4f6;
        font-weight: bold;
    }

    td.heat1 {
        background: #ffb3b3;
        font-weight: bold;
    }
    </style>

    <div class="hall-wrap">
    <table class="hall">
    """

    for row in rows:
        table += "<tr>"

        for col in cols:
            seat = seat_by_position.get((row, col))

            if seat is None:
                table += '<td class="blank"></td>'
                continue

            value = html.escape(str(seat.number))

            if selected_seat is not None and seat.number == selected_seat:
                css = "selected"
            elif seat.zone.name == "Promotion":
                css = "promotion"
            elif seat.zone.name == "NewMachine":
                css = "newmachine"
            else:
                diff = seat.state.diff

                if diff >= 3000:
                    css = "heat4"
                elif diff >= 1000:
                    css = "heat3"
                elif diff >= 0:
                    css = "heat2"
                else:
                    css = "heat1"

            table += f'<td class="{css}">{value}</td>'

        table += "</tr>"

    table += """
    </table>
    </div>
    """

    st.markdown(table, unsafe_allow_html=True)