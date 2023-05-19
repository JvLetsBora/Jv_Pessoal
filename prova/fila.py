""" Implementação da estrutura de dados "fila" """
lista = [[0.0, 0.5],

[0.5, 0.0],

[0.0, 0.5],

[0.5, 0.0],

[0.0, 1.0],

[1.0, 0.0] ]


class Fila:
    def __init__(self):
        self.__queue = []

    def enqueue(self, value):
        self.__queue.append(value)

    def dequeue(self):
        return self.__queue.pop(0)

    def show(self):
        #print(f"Queue: {self.__queue}")
        return self.__queue

    def chamada(self):
        x,y = self.__queue[0][0], self.__queue[0][1]
        #print(f'x:{x}, y:{y}')
        return x, y
    


def main():
    queue = Fila()

    for a in lista:
        queue.enqueue(a)

    print(len(queue.show()))
    queue.chamada()


if __name__ == "__main__":
    main()