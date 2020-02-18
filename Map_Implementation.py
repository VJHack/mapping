import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def cart2pol(self, xCord, yCord):
    r = np.sqrt(xCord ** 2 + yCord ** 2)
    theta = np.arctan2(yCord, xCord)
    return [r, theta]


def pol2cart(self, r, theta):
    xCord = r * np.cos(theta)
    yCord = r * np.sin(theta)
    return [xCord, yCord]

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + np.math.cos(angle) * (px - ox) - np.math.sin(angle) * (py - oy)
    qy = oy + np.math.sin(angle) * (px - ox) + np.math.cos(angle) * (py - oy)
    return qx, qy

#This Map_Implementation is what happens "behind the scenes". How the map actually works. (JUST USE THE INTERFACE)
class Map_Implementation:
    plt.ion()
    mpl.style.use('default')
    def draw_local_plot(self, xBarrArr, yBarrArr, xGlobalBarrArr, yGlobalBarrArr):
        #Setting the size of the figure
        plt.figure(figsize=(16, 8))

        #ax will refer to the local plot
        ax = plt.subplot(121)

        #Setting the limits for the X and Y axis. The local plot is zoomed in on the global
        plt.autoscale(enable=True, axis='both')

        #The arrow shows the direction the car is facing
        plt.arrow(0,0,0, 3, width=0.15, head_width=0.3)

        #plotting the points on the local
        xPoints = xBarrArr
        yPoints = yBarrArr
        ax.scatter(xPoints, yPoints)

        #Adding the values to the global array
        xGlobalBarrArr = xGlobalBarrArr + [xBarrArr[i] for i in range(len(xBarrArr))]
        yGlobalBarrArr = yGlobalBarrArr + [yBarrArr[i] for i in range(len(yBarrArr))]
        print(xGlobalBarrArr)
        print(yGlobalBarrArr)

        #Adds style to the map
        plt.title("Local Map")
        plt.grid(b=True, which='major', color='b', linestyle='-')
        plt.tight_layout()
        return (xGlobalBarrArr,yGlobalBarrArr)


    def draw_global(self, car_posX, car_posY, xGlobalBarrArr, yGlobalBarrArr, offset):
        #the global plot is referred to as bx
        bx = plt.subplot(122)
        plt.plot(car_posX, car_posY, "x")

        #Setting up the arrow
        velocityY = 3 * np.math.cos(np.math.radians(offset))
        velocityX = 3 * np.math.sin(np.math.radians(offset))
        plt.arrow(car_posX,car_posY,velocityX, velocityY, width=0.05, head_width=0.25)

        #rotating and translating the local points onto the global map
        for i in range(0, len(xGlobalBarrArr)):
            xGlobalPoint = xGlobalBarrArr[i] + car_posX
            yGlobalPoint = yGlobalBarrArr[i] + car_posY
            cartTranslate = rotate((car_posX,car_posY), (xGlobalPoint, yGlobalPoint), np.radians(-offset))
            xGlobalBarrArr[i] = cartTranslate[0]
            yGlobalBarrArr[i] = cartTranslate[1]
        print(xGlobalBarrArr)
        print(yGlobalBarrArr)
        """ THE ARRAYS FOR THE GLOBAL POINTS ARE CALLED: xGLobalBarrArr and yGlobalBarrArr """

        #Plotting
        bx.plot(xGlobalBarrArr, yGlobalBarrArr, "o", color='red')
        plt.title("Global Map")

        #Adding Style to the local map
        plt.autoscale(enable=True, axis='both')
        plt.grid(b=True, which='major', color='b', linestyle='-')
        plt.show()
        plt.pause(100)
        Map_Implementation.plt.close('all')