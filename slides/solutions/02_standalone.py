from mayavi import mlab
import numpy as np
from numpy import pi, sin, cos

phi, theta = np.mgrid[0:pi:20j, 0:2*pi:20j]
x = sin(phi)*cos(theta)
y = sin(phi)*sin(theta)
z = cos(phi)
mlab.clf()
mlab.mesh(x, y, z, scalars=z, representation='wireframe')
mlab.colorbar(orientation='vertical')
mlab.title('Sphere')
mlab.outline()
mlab.axes()
mlab.xlabel('X')
mlab.ylabel('Y')
mlab.savefig('sphere.png')
mlab.show()
