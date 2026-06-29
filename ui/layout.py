import html

import streamlit as st


def show_layout(store):
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
    .seat {
        background: #f3f4f6;
        font-weight: bold;
    }

    .promotion {
        background: #b7f7c3;
        font-weight: bold;
    }

    .newmachine {
        background: #b9d9ff;
        font-weight: bold;
    }
    td.blank {
        background: white;
        border-color: #f5f5f5;
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
            else:
                value = html.escape(str(seat.number))
                zone = seat.zone.name

                if zone == "Promotion":
                    css = "promotion"
                elif zone == "NewMachine":
                    css = "newmachine"
                else:
                    css = "seat"

                table += f'<td class="{css}">{value}</td>'

        table += "</tr>"

    table += """
    </table>
    </div>
    """

    st.markdown(table, unsafe_allow_html=True)