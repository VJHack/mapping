from Map_Implementation import Map_Implementation

#This main class is the interface for the map where you just plug in the inputs and the program outputs a map
class Main:

    #plots the local, global, and finished maps
    def plot(self, car_posX, car_posY, xBarrArr, yBarrArr, xGlobalBarrArr, yGlobalBarrArr, offset):
        Map = Map_Implementation
        #Creates the local map
        globalBarrArr = Map.draw_local_plot(self, xBarrArr, yBarrArr, xGlobalBarrArr, yGlobalBarrArr)
        #Creates the global map
        Map.draw_global(self, car_posX, car_posY, globalBarrArr[0], globalBarrArr[1], offset)

    #initializes the variables and calls plot
    def main(self):
        car_posX = int(input("What is the X position of your car?"))
        car_posY = int(input("What is the Y position of your car?"))
        self.plot(car_posX, car_posY, xBarrArr = [5, 5, -5, -5], yBarrArr = [-5, 5, -5, 5], xGlobalBarrArr = [],
                  yGlobalBarrArr = [], offset = int(input("How many degrees would you line the car offset by?")))

if __name__ == '__main__':
    Main().main()