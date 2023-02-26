import pyuff
import numpy as np
import numpy as np
from three import *
import os
import sys

def compute_normals(pts, faces_index):
    print('Computing normals...be patient')
    normals = np.zeros((len(faces_index), 3))
    for (i,face) in enumerate(faces_index):
        a = str(pts[face[0]])
        b = str(pts[face[1]])
        c = str(pts[face[2]])
        d = face[0]
        e = face[1]
        f = face[2]
        curr = np.cross(pts[face[1]] - pts[face[0]], 
            pts[face[2]] - pts[face[0]])
        normals[i] = curr / np.linalg.norm(curr)
        input('**** %d ****\n%s\n%s\n%s\n    ----> %s\n\n'%(i,a,b,c, str(normals[i])))
    return normals

def go(bunny):
    unv_file = pyuff.UFF('unv_files/housing_40k.unv')
    unv_file.get_set_types()
    data = unv_file.read_sets()

    coord = data[2]
    coord.keys()

    x = coord['x']
    y = coord['y']
    z = coord['z']

    Value = data[4]
    val = Value['data_at_node']
    heat = np.array(val)

    x = x.reshape(-1, 1)
    y = y.reshape(-1, 1)
    z = z.reshape(-1, 1)

    data_motor = np.concatenate([x, y, z, heat], 1)

    # # Compute the convex hull of the dataset
    # hull = ConvexHull(data_motor)

    # # Extract the vertices of the boundary facets
    # boundary_points = np.unique(hull.vertices)

    mesh_info = data[3]

    points = data_motor[:,:3]
    colors = np.array(data[4]['data_at_node'])
    normals = compute_normals(points, mesh_info['triangle']['nodes_nums'])

    #colors = np.random.random((len(colors), 3))
    colors = np.ones((len(colors), 3))
    
    np.save("points.npy", points)
    np.save("colors.npy", colors)
    np.save("normals.npy", normals)

    print('Invoking three.py!')
    os.system('python three.py %s'%str(bunny))

if( __name__ == "__main__" ):
    bunny = False if len(sys.argv) == 1 else sys.argv[1].lower() == 't'
    if( bunny ): print('BUNNY')
    else: print('AWS CHALLENGE')
    go(bunny)