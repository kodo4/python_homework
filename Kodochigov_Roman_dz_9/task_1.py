import time


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self, r, y, g):
        timing = [r, y, g]
        while True:
            for i in range(len(self.__color)):
                print(__color[i])
                time.sleep(timing[i])


crossroad = TrafficLight()
crossroad.running(7, 2, 5)
