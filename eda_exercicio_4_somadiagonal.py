def somaDiagonal(matriz):
    soma = 0
    for i in range(int(x)):
        soma += matriz[i][i]
    return soma


x, y = input().split()
matriz = []
for i in range(int(x)):
    lista = [int(z) for z in input().split()]
    matriz.append(lista)
print(somaDiagonal(matriz))