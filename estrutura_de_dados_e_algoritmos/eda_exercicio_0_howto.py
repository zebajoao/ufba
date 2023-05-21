def howto(matriz, soma=0, media=0):
    for i in range(len(matriz)):
        j = len(matriz[i]) - 1
        soma += matriz[i][j]
    media = soma / len(matriz)
    return media


lista = [float(x) for x in input().split()]
numLinhas = int(lista[0])
matriz = []
for i in range(numLinhas):
    linha = [float(x) for x in input().split()]
    matriz.append(linha)
linhaTeste = int(lista[1]) - 1
matriz.reverse()
matriz.remove(matriz[linhaTeste])
print(howto(matriz))