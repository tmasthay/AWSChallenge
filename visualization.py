import numpy as np
import pyvista
import pyuff
import PVGeo

unv_file = pyuff.UFF('unv_files/housing_40k.unv')
unv_file.get_set_types()
data = unv_file.read_sets()
data
coord = data[2]
coord
coord.keys()
x = coord['x']
y = coord['y']
z = coord['z']
print(x)
print(type(x))
print(np.shape(x))
Value = data[4]
val = Value['data_at_node']
heat = np.array(val)
x = x.reshape(-1, 1)
y = y.reshape(-1, 1)
z = z.reshape(-1, 1)
#point_cloud = np.random.random((100, 3))
pdata = pyvista.PolyData(np.concatenate([x, y, z], 1) #, heat
)
grid = PVGeo.filters.VoxelizePoints().apply(pdata)
p = pyvista.Plotter(notebook=0)
p.add_mesh(grid, opacity=0.5, show_edges=True)
p.add_mesh(pdata, point_size=5, color="red")
p.show_grid()
p.show()


#voxel_grid = pdata.voxelize(0.05)  # 0.05 is the voxel size in units of the point cloud
#voxel_grid = pdata.voxel_down_sample(0.05)  # 0.05 is the voxel size in units of the point cloud

#voxel_grid.plot()

# Create surface mesh
surf_mesh = pdata.delaunay_3d()
# Plot point cloud mesh
#pdata.plot()
# Plot surface mesh
surf_mesh.plot()

#surf = points.reconstruct_surface()
#pdata['orig_sphere'] = np.arange(100)

# create many spheres from the point cloud
#sphere = pyvista.Sphere(radius=0.02, phi_resolution=10, theta_resolution=10)
#pc = pdata.glyph(scale=False, geom=sphere, orient=False)
#pc.plot(cmap='Reds')