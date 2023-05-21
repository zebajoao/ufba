def somaColuna(matriz):
    matrizTransposta = []
    for i in range(int(y)):
        lista = []
        for j in range(int(x)):
            lista.append(matriz[j][i])
        matrizTransposta.append(lista)
    soma = 0
    for i in range(int(y)):
        soma += matrizTransposta[i][0]
    return soma


x, y = input().split()
matriz = []
for i in range(int(x)):
    lista = [int(z) for z in input().split()]
    matriz.append(lista)
print(somaColuna(matriz))