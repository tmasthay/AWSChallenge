import numpy as np
import pyvista
import pyuff
import PVGeo
import sys

def extract_data(filename):
    unv_file = pyuff.UFF(filename)
    unv_file.get_set_types()
    data = unv_file.read_sets()
    coord = data[2]
    x = coord['x'].reshape(-1,1)
    y = coord['y'].reshape(-1,1)
    z = coord['z'].reshape(-1,1)
    heat = np.array(data[4]['data_at_node'])
    pdata = pyvista.PolyData(np.concatenate([x, y, z], 1))
    pdata["Temperature"] = heat
    return pdata

def plot_voxel_data(pdata, point_size=15, cmap="coolwarm"):
    grid = PVGeo.filters.VoxelizePoints().apply(pdata)
    p = pyvista.Plotter(notebook=0)
    p.add_mesh(pdata, point_size=point_size, scalars="Temperature", cmap=cmap)
    p.show_grid()
    p.show()

if( __name__ == "__main__" ):
    pdata = extract_data('unv_files/housing_40k.unv')
    plot_voxel_data(pdata, point_size=15, cmap="coolwarm")


    # Create surface mesh
    #surf_mesh = pdata.delaunay_3d(alpha=9.0)
    # Plot surface mesh
    #surf_mesh.plot()
    # Plot point cloud mesh
    #pdata.plot()


    #voxel_grid = pdata.voxelize(0.05)  # 0.05 is the voxel size in units of the point cloud
    #voxel_grid = pdata.voxel_down_sample(0.05)  # 0.05 is the voxel size in units of the point cloud