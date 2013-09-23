# -*- coding: utf-8 -*-


import threading

semaphore_writer = threading.Semaphore(1)
semaphore_reader = threading.Semaphore(0)

myList = []


class Writer(threading.Thread):

    def __init__(self, numbOfThread, elem):
        threading.Thread.__init__(self)
        self.x = numbOfThread
        self.y = elem

    def putElement(self):
        semaphore_writer.acquire()
        myList.append(self.y)
        semaphore_writer.release()
        semaphore_reader.release()

    def run(self):
        while (True):
            self.putElement()
            print (("Thread N:  " + str(self.x) + "put value:   "
            + str(self.y)))


class Reader(threading. Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def readElement(self):
        semaphore_reader.acquire()
        semaphore_writer.acquire()
        print((myList[0]))
        myList.pop(0)
        semaphore_writer.acquire()

    def run(self):
        while(True):
            self.readElement()

#Monitor


class MList():

    def __init__(self, myList2):
        self.myList2 = myList2
        self.lock = threading.Lock()
        self.condition = threading.Condition()

    def putElement(self, x):
        self.myList2.append(x)

    def readElement(self):
        try:
            self.lock.acquire()
            while (len(self.myList2) == 0):
                self.condition.wait()
                print((self.myList2[0]))
                self.myList2.pop(0)
        finally:
            self.lock.release()


class MWriter(threading.Thread):

    def __init__(self, mList, myId):
        threading.Thread.__init__(self)
        self.mList = mList
        self.id = myId

    def run(self):
        while (True):
            self.mList.putElement(self.id)
            self.mList.condition.release()


class MReader(threading.Thread):

    def __init__(self, mylist):
        threading.Thread.__init__(self)
        self.myList = myList

    def run(self):
        while(True):
            self.mList.readElement()


def main():
    h = Writer(0, 'a')
    x = Writer(1, 'b')
    y = Writer(2, 'c')
    z = Writer(3, 'd')
    k = Reader()
    m = Reader()
    g = Reader()
    a = Reader()
    h.start()
    x.start()
    y.start()
    z.start()
    k.start()
    m.start()
    g.start()
    a.start()


if __name__ == '__main__':

    main()