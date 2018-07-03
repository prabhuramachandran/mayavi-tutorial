x, y, z = mgrid[-50:50:20j,-50:50:20j, -10:60:20j]
u, v, w = lorenz(x, y, z)

mlab.clf()
mlab.quiver3d(
    x, y, z, u, v, w,
    scale_factor=0.01,
    mask_points=5
)
