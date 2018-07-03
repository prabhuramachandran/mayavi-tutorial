def lorenz_ode(state, t):
    x, y, z = state
    return np.array(lorenz(x, y, z))

t = np.linspace(0., 50., 2000)
r = odeint(
    lorenz_ode, (10., 50., 50.), t
)

#x, y, z = r[:,0], r[:,1], r[:,2]
x, y, z = r.T
mlab.plot3d(x, y, z, t, tube_radius=None)
