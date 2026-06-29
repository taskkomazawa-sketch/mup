import html

import streamlit as st


def show_layout(store):
    st.divider()
    st.subheader("Hall Layout")

    max_row = max(cell.row for cell in store.cells)
    max_col = max(cell.col for cell in store.cells)

    cell_map = {
        (cell.row, cell.col): cell
        for cell in store.cells
    }

    table = """
    <style>
      .hall-wrap {
        overflow-x: auto;
        border: 1px solid #ddd;
        padding: 8px;
        background: #fafafa;
      }
      table.hall {
        border-collapse: collapse;
        table-layout: fixed;
      }
      table.hall td {
        width: 42px;
        height: 28px;
        min-width: 42px;
        max-width: 42px;
        border: 1px solid #e0e0e0;
        text-align: center;
        vertical-align: middle;
        font-size: 11px;
        white-space: nowrap;
      }
      td.seat {
        background: #f1f3f5;
        font-weight: 700;
      }
      td.aisle {
        background: #ffffff;
        color: #cccccc;
      }
      td.blank {
        background: #ffffff;
        border-color: #ffffff;
      }
    </style>
    <div class="hall-wrap">
    <table class="hall">
    """

    for row in range(1, max_row + 1):
        table += "<tr>"

        for col in range(1, max_col + 1):
            cell = cell_map.get((row, col))

            if cell is None or cell.value is None:
                table += '<td class="blank"></td>'
                continue

            value = html.escape(str(cell.value))

            if isinstance(cell.value, int):
                table += f'<td class="seat">{value}</td>'
            else:
                table += f'<td class="aisle">{value}</td>'

        table += "</tr>"

    table += """
    </table>
    </div>
    """

    st.markdown(table, unsafe_allow_html=True)