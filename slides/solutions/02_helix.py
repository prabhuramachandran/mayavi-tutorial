mlab.clf()

t = linspace(0, 10*pi, 1000)
x, y = 0.2*sin(t), 0.2*cos(t)
z = 0.1*t
mlab.plot3d(x, y, z, color=(1, 0, 0))
mlab.points3d(x[-1], y[-1], z[-1])
