import numpy as np

class ht:
    def generate_cylinder(radius, height, direction_vector, num_points):
        # Normalize the direction vector
        direction_vector = direction_vector / np.linalg.norm(direction_vector)
        
        # Generate the points on the cylinder surface
        theta = np.linspace(0, 2*np.pi, num_points)
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        z = np.linspace(0, height, num_points)
        
        # Calculate the rotation matrix to align the cylinder with the direction vector
        v = np.array([0, 0, 1]) # the default direction of the cylinder
        if np.allclose(direction_vector, v):
            # the direction vector is already aligned with the cylinder, no rotation needed
            R = np.identity(3)
        else:
            # calculate the rotation axis and angle between the default direction and the direction vector
            axis = np.cross(v, direction_vector)
            angle = np.arccos(np.dot(v, direction_vector))
            # calculate the rotation matrix
            axis = axis / np.linalg.norm(axis)
            c = np.cos(angle)
            s = np.sin(angle)
            R = np.array([[c + axis[0]**2*(1-c), axis[0]*axis[1]*(1-c)-axis[2]*s, axis[0]*axis[2]*(1-c)+axis[1]*s],
                        [axis[1]*axis[0]*(1-c)+axis[2]*s, c+axis[1]**2*(1-c), axis[1]*axis[2]*(1-c)-axis[0]*s],
                        [axis[2]*axis[0]*(1-c)-axis[1]*s, axis[2]*axis[1]*(1-c)+axis[0]*s, c+axis[2]**2*(1-c)]])
        
        # Apply the rotation matrix to the points to align the cylinder with the direction vector
        points = np.stack((x, y, z), axis=-1)
        points = np.matmul(points, R)
        
        return points
    
    def cut_cylinder(pts, p0, r0):
        length = np.linalg.norm(p0)
        assert(length > 0)
        p0 = p0 / length
        interior = []
        boundary = []
        for pt in pts:
            alpha = np.dot(pt, p0)
            r = np.linalg.norm(pt - alpha * p0)
            if( r < r0 ):
                interior.append(pt)
            else:
                boundary.append(pt)
        return interior, boundary

    def cut_cube(pts, p0, beta, gamma):
        length = np.linalg.norm(p0)
        assert( length > 0.0 )
        p0 = p0 / length
        in_cube, not_in_cube = [], []
        for pt in pts:
            alpha = np.dot(pt, p0)
            if( beta <= alpha and alpha <= gamma ):
                
            else:
                not_in_cube.append(pt)
        return pts
