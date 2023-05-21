import numpy as np


def produtoInterno(vetor1, vetor2, produtoInterno = 0):
    if len(vetor1) <= len(vetor2):
        for i in range(len(vetor1)):
            produtoInterno += (vetor1[i]*vetor2[i])
    else:
        for i in range(len(vetor2)):
            produtoInterno += (vetor1[i]*vetor2[i])
    return produtoInterno


vetor1 = np.array(input().split(), dtype = int)
vetor2 = np.array(input().split(), dtype = int)
print(produtoInterno(vetor1, vetor2))