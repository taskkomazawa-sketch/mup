from engine.layout.loader import LayoutLoader


def test_layout_load():

    loader = LayoutLoader(
        "data/layouts/minowa_uno_coordinate_map.xlsx"
    )

    cells = loader.load()

    assert len(cells) > 1000