from cNo import *

class ListaEncadeadaCircular:
    def __init__(self):
        self.head = None
        self.tail= None
    
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
            self.setTail(elemento)
        elemento.setProximo(self.getHead())
            
    def empty(self):
        if self.getHead() == None:
            return True
        return False
    
    def freeList(self):
        self.setHead(None)
        self.setTail(None)
    
    def total(self):
        valor = 0
        temp = self.getHead()
        while True:
            vetor = temp.getInfo()
            valor += int(vetor[1])
            if temp.getProximo() == self.getHead():
                break
            temp = temp.getProximo()
        return valor
        
    def search(self, total):
        temp = self.getHead()
        for i in range(total):
            temp = temp.getProximo()
        vetor = temp.getInfo()
        print(vetor[0])