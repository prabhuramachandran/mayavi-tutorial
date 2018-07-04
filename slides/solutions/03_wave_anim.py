import time
for i in range(25):
    s.mlab_source.scalars = np.sin((x*x + y*y) + 8*np.pi*i/25)
    mlab.process_ui_events()
    mlab.savefig('/tmp/anim_%03d.png')
    time.sleep(0.05)
