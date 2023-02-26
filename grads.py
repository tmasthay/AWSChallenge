from visualization import *

def build_neighbors(pts, cells, k=3):
    neighbors = 1e6 * np.zeros((len(pts), k))
    min_dists = np.inf * np.ones((len(neighbors), 3))
    for c in cells:
        for i in c:
            others = set(c).difference(set([i]))
            for o in others:
                try:
                    curr = np.linalg.norm(pts[i-1] - pts[o-1])
                    j = 0
                    while( j < k ):
                        if( curr < min_dists[i-1][j] ): break
                        else: j += 1
                    if( j < k ):
                        neighbors[i-1][j] = o-1
                        min_dists[i-1][j] = curr 
                    for l in range(1,k):
                        assert(min_dists[i-1,l-1] <= min_dists[i-1,l])
                except:
                    print('Something wrong in build_neighbors, (o,i) = (%d,%d)'%(o,i))
                    raise
    return neighbors

pdata, x, y, z, f, data = extract_data('unv_files/housing_40k.unv')

mesh_info = data[3]
pts = np.array([e for e in zip(x,y,z,f)])
triangles_faces = mesh_info['triangle']['nodes_nums']
quad_faces = mesh_info['quad']['nodes_nums']
neighbor_tri = build_neighbors(pts, triangles_faces)
neighbor_quad = build_neighbors(pts, quad_faces)

neighbors = [np.array(np.unique(np.append(e,ee)), dtype=int) for (e,ee) in zip(neighbor_tri, neighbor_quad)]