import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections as mc

# ==================== Sample Data ====================== #

sampleBarriers = np.array([[-10, -20, -10, 20], [-10, 20, 10, 20]], float)
sampleObs = np.array([[10, 0, 40], [20, 0, 80], [30, 0, 160]], float)
sampleState = np.array([0, 0, 0])

# ===================== Functions ======================= #


# converts 2D sampleBarriers array to 3D for the LineCollection method
# LineCollection method (barrier plotter) has parameter --> [x1,y1] , [x2,y2]
def _2d_to_3d_(box):
    i = 0
    while i < len(sampleBarriers):
        z = np.split(sampleBarriers[i], 2)
        x = np.vstack((z[0], z[1]))
        lines = np.array([x])
        box = np.concatenate((box, lines))
        i += 1
    return box

def cart2polar(x, y):
    r = np.sqrt(x ** 2 + y ** 2)
    rad = np.arctan2(y, x)
    return r, rad   # r = radius , rad = angle

def polar2cart(r, rad):
    x = r * np.cos(rad)
    y = r * np.sin(rad)
    return x, y

# one to two dimensional array conversion
def chunks(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

# translates the barriers from the global map to the local so that the lines are with respect
# to the car's x, y and heading --> carX, carY, carRad
def local2Global(carX, carY, carRad):
    adjX = middleMan[:, :, 0].flatten() + carX
    adjY = middleMan[:, :, 1].flatten() + carY
    a = cart2polar(adjX, adjY)
    adjRad = a[1] + carRad
    b = polar2cart(a[0], adjRad)
    bruh = [None]*(len(b[0])+len(b[1]))
    bruh[::2] = b[0]
    bruh[1::2] = b[1]
    final = chunks(chunks(bruh, 2), 2)
    return final


# ================== Function Calls  =================== #


box = np.array([[[0, 0], [0, 0]]], float)  # initialized to allow for concatenation; gets deleted
localBarriers = np.delete(_2d_to_3d_(box), 0, 0)  # <-------- Final local barrier array
middleMan = np.delete(_2d_to_3d_(box), 0, 0)  # intermediary array used to translate local --> global barriers
localObs = np.stack(sampleObs, axis=-1)  # <-------- FINAL obstacle array


carHead = polar2cart(10, sampleState[2] + np.pi/2)  # car heading ; length of arrow = 10
a = cart2polar(sampleState[0], sampleState[1])
b = a[1] + sampleState[2]
carGlob = polar2cart(a[0], b)
globalBarriers = local2Global(sampleState[0], sampleState[1], sampleState[2])  # <--- FINAL global barrier array

# ===================== Plotting ======================== #


fig = plt.figure(figsize=(12,7))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.set(xlim=(-50, 50), ylim=(-50, 50))
ax2.set(xlim=(-50, 50), ylim=(-50, 50))

ax1.plot(0, 0, "o", color='ORANGE')  # local Car
ax2.plot(carGlob[0], carGlob[1], "o", color='ORANGE')  # lobal Car
ax1.arrow(0, 0, 0, 10, width=0.5, head_width=5, head_length=5,
          overhang=0.5, color='ORANGE')
ax2.arrow(carGlob[0], carGlob[1], carHead[0], carHead[1], width=0.5,
          head_width=5, head_length=5, overhang=0.5, color='ORANGE')

lc = mc.LineCollection(globalBarriers, linewidths=2)
ax2.add_collection(lc)
lc2 = mc.LineCollection(localBarriers, linewidths=2)
ax1.add_collection(lc2)
ax1.scatter(localObs[0], localObs[1], s=localObs[2])

ax1.grid(linestyle='-', linewidth='0.5', color='black')
ax2.grid(linestyle='-', linewidth='0.5', color='black')
ax1.set_title("Local Map", color="Blue")
ax2.set_title("Global Map", color="Brown")

plt.show()


