from cNo import *

class Pilha:
    def __init__(self):
        self.top = None
    
    def getTop(self):
        return self.top
    
    def setTop(self, no):
        self.top = no
    
    def empty(self):
        if self.getTop() == None:
            return True
        return False
    
    def push(self, valor):
        elemento = No(valor)
        if self.empty():
            self.setTop(elemento)
        else:
            elemento.setProximo(self.getTop())
            self.setTop(elemento)
    
    def pop(self):
        if self.empty():
            print("Erro -> Pilha vazia!")
        else:
            temp = self.getTop()
            self.setTop(temp.getProximo())
            temp.setProximo(None)
            return temp.getValor()