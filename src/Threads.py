# -*- coding: utf-8 -*-
import threading
import time

lista = ['a', 'b', 'c', 'd', 'e', 'f']
semaphore = threading.Semaphore(1)


class Threads(threading.Thread):

    def __init__(self, num):
        threading.Thread.__init__(self)
        self.number = num

    def run(self):
        while(True):
            lista.pop(0)
            time.sleep(3)
            for i in range(len(lista)):
                print (("Thread number :   " + str(self.number)
                      + str(lista[i])))


def main():
    x = Threads(1)
    y = Threads(2)
    z = Threads(3)
    x.start()
    y.start()
    z.start()

if __name__ == '__main__':

    main()
