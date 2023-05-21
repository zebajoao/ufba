from cNo import *

class ListaDplEncadeada:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def getHead(self):
        return self.head
    
    def setHead(self, no):
        self.head = no
        
    def getTail(self):
        return self.tail
    
    def setTail(self, no):
        self.tail = no
    
    def append(self, valor):
        elemento = No(valor)
        if self.empty():
            self.setHead(elemento)
            self.setTail(elemento)
        else:
            temp = self.getTail()
            temp.setProximo(elemento)
            elemento.setAnterior(temp)
            self.setTail(elemento)
    
    def display(self):
        if self.empty():
            print("Erro -> Lista vazia!")
        else:
            temp = self.getHead()
            print('[', end='')
            while temp != self.getTail():
                print(f"{temp.getValor()}", end=", ")
                temp = temp.proximo
            print(f"{temp.getValor()}", ']', sep='')
      
    def empty(self):
        if self.getHead() == None:
            return True
        return False
    
    def freeList(self):
        self.setHead(None)
        self.setTail(None)  
    
    def search(self, lista):
        caminho = ListaDplEncadeada()
        temp = lista.getHead()
        temp2 = temp.getAnterior()
        temp3 = self.getHead()
        while True:
            if temp2 == None or temp.getValor() >= temp2.getValor():
                while temp3.getValor() < temp.getValor() and temp3.getProximo() != None:
                    caminho.append(temp3.getValor())
                    temp3 = temp3.getProximo()
                caminho.append(temp3.getValor())
            else:
                while temp3.getValor() > temp.getValor() and temp3.getAnterior() != None:
                    caminho.append(temp3.getValor())
                    temp3 = temp3.getAnterior()
                caminho.append(temp3.getValor())
            temp = temp.getProximo()
            if temp == None:
                break
            temp2 = temp.getAnterior()
        return caminho
    '''
    def newList():
        return ListaDplEncadeada()
    '''
    
    