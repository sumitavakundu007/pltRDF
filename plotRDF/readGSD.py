import gsd
import gsd.hoomd

def readGSD_func(input_gsd):
    f = gsd.hoomd.open(name=input_gsd, mode='rb')
    snap = f[-1]
    num_particles = snap.particles.N
    positions = snap.particles.position
    box = snap.configuration.box

    return num_particles, positions, box
