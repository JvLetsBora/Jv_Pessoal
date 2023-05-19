"""Implementação da estrutura de dados 'Pilha'"""


class Pilha():
    def __init__(self):
        self.__stack = []

    def _push(self, value=[]):
        self.__stack.append(value)

    def pop(self):
        self.__stack.pop()
        

    def show(self):
        return self.__stack
    
    def chamada(self):
        x,y = self.__stack[len(self.show())-1]
        return x,y

