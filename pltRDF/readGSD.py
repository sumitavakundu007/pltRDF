import gsd
import gsd.hoomd
from freud import box

def readGSD_func(input_gsd):
    f = gsd.hoomd.open(name=input_gsd, mode='rb')
    snap = f[-1]
    positions = snap.particles.position
    Box = snap.configuration.box
    box_arr = box.Box(Lx=Box[0], Ly=Box[1], Lz=Box[2],
                    xy=Box[3], xz=Box[4], yz=Box[5], is2D=False)

    return positions, box_arr