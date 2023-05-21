from cNo import *


class ListaEncadeadaSimples:

    def __init__(self):
        self.head = None

    def getHead(self):
        return self.head

    def setHead(self, elemento):
        self.head = elemento

    def append(self, elemento):
        if self.getHead() == None:
            self.setHead(elemento)
        else:
            temp = self.getHead()
            while temp.prox != None:
                temp = temp.prox
            temp.prox = elemento

    def display(self):
        if self.getHead() == None:
            print("Erro -> Lista vazia!")
        else:
            print('[', end='')
            temp = self.getHead()
            while temp.prox != None:
                print(f"{temp.valor},", end=' ')
                temp = temp.prox
            print(temp.valor, ']', sep='')

    def freeList(self):
        self.setHead(None)

    def insert(self, elemento, indice):
        temp = self.getHead()
        if indice == 0:
            if elemento.prox != None:
                temp2 = elemento
                while temp2.prox != None:
                    temp2 = temp2.prox
                temp2.prox = temp.prox
            else:
                elemento.prox = temp
            self.setHead(elemento)
        else:
            for i in range(indice - 1):
                temp = temp.prox
            if elemento.prox != None:
                temp2 = elemento
                while temp2.prox != None:
                    temp2 = temp2.prox
                temp2.prox = temp.prox
            else:
                elemento.prox = temp.prox
            temp.prox = elemento
    
    def remove(self):  #remove repetições
        listaTemp = ListaEncadeadaSimples()
        temp = self.getHead()
        temp2 = temp.prox
        while temp2 != None:
            if listaTemp.search(temp2.valor):
                temp.prox = temp2.prox
            else:
                listaTemp.append(No(temp.valor))
                temp = temp.prox
            temp2 = temp2.prox 
        
    def search(self, valor):
        temp = self.getHead()
        while temp != None:
            if temp.valor == valor:
                return True
            temp = temp.prox
        return False