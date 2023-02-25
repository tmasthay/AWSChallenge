import numpy as np

def cut_cylinder(pts, p0, r0):
    assert(np.linalg.norm(p0) > 0)
    interior = []
    boundary = []
    for pt in pts:
        alpha = np.dot(pt, p0) / np.linalg.norm(p0)
        r = np.linalg.norm(pt - alpha * p0)
        if( r < r0 ):
            interior.append(pt)
        else:
            boundary.append(pt)
    return interior, boundary

def cut_cube(pts, p0, alpha, beta):
    return 'table this'

