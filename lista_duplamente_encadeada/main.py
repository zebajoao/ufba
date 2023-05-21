import numpy as np
from cListaDuplaEncad import *

def newList():
    return ListaDplEncadeada()

def main():
    print("Testando lista duplamente encadeada...")
    qtdLinhas = int(input())
    vetor1 = np.array(input().split(), dtype=int)
    vetor2 = np.array(input().split(), dtype=int)
    lista1 = newList()
    for i in range(len(vetor1)):
        lista1.append(vetor1[i])
    lista2 = newList()    
    for i in range(len(vetor2)):
        lista2.append(vetor2[i])    
    print()
    caminho = lista1.search(lista2)
    caminho.display()
    
if __name__ == "__main__":
    main()