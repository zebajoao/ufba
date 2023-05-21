from cListaEncadeadaCircular import *
import numpy as np

def main():
    print("Testando lista encadeada circular...")
    lista = ListaEncadeadaCircular()
    qtdLinhas = int(input())
    for i in range(qtdLinhas - 1):
        vetor = np.array(input().split(), dtype=str)
        lista.append(vetor)
    total = lista.total()
    lista.search(total)
    
if __name__ == "__main__":
    main()