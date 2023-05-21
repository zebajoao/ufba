from cListaEncadeada import *
from cNo import *
import numpy as np


def newList():
    return ListaEncadeadaSimples()


def main():
    print("Testando lista encadeada simples")
    
    '''
    lista = newList()
    lista.append(No(5))
    lista.append(No(8))
    lista.append(No(2))
    lista.display()
    lista.insert(No(7), 0)
    lista.display()
    lista.insert(No(1), 2)
    lista.display()
    lista.freeList()
    lista.display()
    '''

    qtdLinhas = int(input())
    lista1 = newList()
    lista2 = newList()
    vetor1 = np.array(input().split(), dtype=int)
    vetor2 = np.array(input().split(), dtype=int)
    for i in range(len(vetor1)):
        lista1.append(No(vetor1[i]))
    for i in range(len(vetor2)):
        lista2.append(No(vetor2[i]))
    indiceInsercao = int(input())
    lista1.insert(lista2.getHead(), indiceInsercao)
    lista1.display()
    lista1.remove()
    lista1.display()


if __name__ == "__main__":
    main()
