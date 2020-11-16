from itertools import cycle
import time


class TrafficLight:
    def __init__(self):
        self.__my_color = 'red'
        self.__list_t = [['red', 7], ['yellow', 2], ['green', 3]]  # список задержек

    def my_running(self, maximum):
        count = 0
        for el1, el2 in cycle(self.__list_t):
            if count >= maximum*3:
                break
            self.__my_color = el1
            print(self.__my_color, ' задержка ', el2)
            time.sleep(el2)
            count += 1


t_l = TrafficLight()
t_l.my_running(3)  # 2 - количество переключений светофора
