# Functions to construct a simple multi-fin heat sink

import build123d as bd

def heat_sink(
        base_width=10,
        base_length=10,
        base_height=2,
        fin_width=0.25,
        fin_height=7,
        nr_fins=10,
): 
    with bd.BuildPart() as bp:
        # Base block
        bd.Box(base_width, base_length, base_height)

        # Create a list of fin locations
        fin_gap = (base_width - fin_width) / (nr_fins - 1)
        first_fin_pos = -(base_width - fin_width) / 2
        positions = []
        for i in range(nr_fins):
            positions.append((
                first_fin_pos + i * fin_gap,
                0.0,
                (base_height + fin_height) / 2,
            ))

        with bd.Locations(*positions):
            bd.Box(fin_width, base_length, fin_height)

    return bp.part

# run if main27
if __name__ == "__main__":
    from ocp_vscode import *
    hs = heat_sink()
    if "show_object" in locals():
        show_object(hs.wrapped, name="heat sink")