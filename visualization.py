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
pdata["Temperature"] = heat
grid = PVGeo.filters.VoxelizePoints().apply(pdata)
p = pyvista.Plotter(notebook=0)
p.add_mesh(pdata, point_size=10, scalars = "Temperature", cmap="coolwarm")
p.show_grid()
p.show()


# Create surface mesh
#surf_mesh = pdata.delaunay_3d(alpha=9.0)
# Plot surface mesh
#surf_mesh.plot()
# Plot point cloud mesh
#pdata.plot()

"""
# fit to unit cube
pcd.scale(1 / np.max(pcd.get_max_bound() - pcd.get_min_bound()),
          center=pcd.get_center())
pcd.colors = o3d.utility.Vector3dVector(np.random.uniform(0, 1, size=(N, 3)))
o3d.visualization.draw_geometries([pcd])

print('voxelization')
voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(pcd,
                                                            voxel_size=0.05)
o3d.visualization.draw_geometries([voxel_grid])
"""

#voxel_grid = pdata.voxelize(0.05)  # 0.05 is the voxel size in units of the point cloud
#voxel_grid = pdata.voxel_down_sample(0.05)  # 0.05 is the voxel size in units of the point cloud

#voxel_grid.plot()


#surf = points.reconstruct_surface()
#pdata['orig_sphere'] = np.arange(100)

# create many spheres from the point cloud
#sphere = pyvista.Sphere(radius=0.02, phi_resolution=10, theta_resolution=10)
#pc = pdata.glyph(scale=False, geom=sphere, orient=False)
#pc.plot(cmap='Reds')