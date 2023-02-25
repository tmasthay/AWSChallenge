import pyvista as pv

# Load the STL mesh
mesh = pv.read('test.stl')

# Render the mesh
mesh.plot()
