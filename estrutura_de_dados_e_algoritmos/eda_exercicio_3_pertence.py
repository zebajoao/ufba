import numpy as np


def pertence(vetor1, vetor2):
    soma = 0
    lista = []
    for i in vetor1:
        if i in vetor2 and i not in lista:
            lista.append(i)
            soma += i
    return soma


vetor1 = np.array(input().split(), dtype=int)
vetor2 = np.array(input().split(), dtype=int)

print(pertence(vetor1, vetor2))