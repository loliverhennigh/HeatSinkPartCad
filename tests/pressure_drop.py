# Pytests for pressure drop produced by the heat sink

import pytest
import gmsh
import build123d as bd

from heat_sink import heat_sink


@pytest.mark.parametrize("base_width", [10])
@pytest.mark.parametrize("base_length", [5, 10, 15])
@pytest.mark.parametrize("base_height", [1, 2, 3])
@pytest.mark.parametrize("fin_width", [0.25])
@pytest.mark.parametrize("fin_height", [7])
@pytest.mark.parametrize("nr_fins", [10])
def test_pressure_drop(base_width, base_length, base_height, fin_width, fin_height, nr_fins):
    # Make a heat sink
    hs = heat_sink(
        base_width=base_width,
        base_length=base_length,
        base_height=base_height,
        fin_width=fin_width,
        fin_height=fin_height,
        nr_fins=nr_fins,
    )

    # Generate a stl file from the heat sink
    hs.export_stl("heat_sink.stl")

    # Generate a mesh from the stl file
    gmsh.initialize()
    gmsh.model.add('model')
    
    # Import STL
    gmsh.model.occ.importShapes('heat_sink.stl')
    gmsh.model.occ.synchronize()
    
    # Set meshing parameters and generate mesh
    gmsh.model.mesh.generate(3)
    
    # Save mesh
    gmsh.write('output_mesh.msh')
    gmsh.finalize()