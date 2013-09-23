class Class():

    def __init__(self, lista):
        self.list = lista

    def prinT(self):
        i = 0
        while (i < len(self.list)):
            print ((self.list[i]))
            i = i + 1
        return i

    def addElement(self, elem):
        self.list.append(elem)

    def firstElement(self):
        return self.list[0]


def main():
    lista = ['hola', 'bien', 'jaja']
    x = Class(lista)
    x.prinT()


if __name__ == '__main__':

    main()