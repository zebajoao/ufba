import numpy as np


# Exercício 1 - Função Multiplica

print("Exercício 1)")
lista = input("\nDigite a seguir os números que gostaria de multiplicar: ").split(sep=' ')
x = int(lista[0])
y = int(lista[1])


def multiplica(x, y):
    if x < y:
        for i in range(y-1):
            x += x
        return x
    else:
        for i in range(x-1):
            y += y
        return y


print(f"\nA multiplicação de {x} por {y} resulta em {multiplica(x, y)}.")
print("-----------------------------------------------------------------\n")


# Exercício 2 - Função Divide

print("Exercício 2)")
lista = input("\nDigite a seguir um dividendo e um divisor: ").split(sep=' ')
x = int(lista[0])
y = int(lista[1])


def divide(x, y):
    if x < y:
        return 0
    else:
        quociente = 1
        while x > y:
            x -= y
            quociente += 1
        return quociente


print(f"\nA divisão de {x} por {y} resulta em {divide(x, y)}.")
print("-----------------------------------------------------------------\n")


# Exercício 3 - Função Potencia

print("Exercício 3)")
lista = input("\nDigite a seguir a base e o expoente da potenciação: ").split(sep=' ')
x = int(lista[0])
y = int(lista[1])


def potencia(x, y):
    if y == 0 or x == 1:
        return 1
    elif x == 0:
        return 0
    else:
        z = 1
        for i in range(y):
            z *= x
        return z


print(f"\n{x} elevado a {y}ª potência resulta em {potencia(x, y)}.")
print("-----------------------------------------------------------------\n")


# Exercício 4 - Função Primo

print("Exercício 4)")
x = int(input("\nDigite a seguir um número para ser identificado: "))


def primo(x):
    if x == 0 or x == 1:
        return 0
    i = 2
    while i < x:
        if x % i == 0:
            return 0
        i += 1
    return 1


if primo(x):
    print("\nEste número é primo.")
else:
    print("\nEste número não é primo.")
print("-----------------------------------------------------------------\n")


# Exercício 5 - Função Fatorial

print("Exercício 5)")
x = int(input("\nDigite a seguir um número para descobrir o seu fatorial: "))


def fatorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        for i in range(x-1, 0, -1):
            x *= i
        return x


print(f"\nO fatorial de {x} é {fatorial(x)}.")
print("-----------------------------------------------------------------\n")


# Exercício 6 - Função Inteiros

print("Exercício 6)")
x = int(input("\nDigite a seguir um número inteiro positivo: "))


def inteiros(x, soma=0):
    for i in range(x+1):
        soma += i
    return soma


print(f"\nA soma de todos os inteiros positivos entre 1 e {x} resulta em {inteiros(x)}.")
print("-----------------------------------------------------------------\n")


# Exercício 7 - Função Fibonacci

print("Exercício 7)")
x = int(input("\nDigite um número a seguir: "))


def fibonacci(x, i=2, y=1, soma=0):
    lista = [0, 1]
    while y <= x:
        y = lista[i-2] + lista[i-1]
        if y > x:
            break
        lista.append(y)
        i += 1
    for j in lista:
        soma += j
    return soma


print(f"\nA soma de sua sequência de Fibonacci resulta em {fibonacci(x)}.")
print("-----------------------------------------------------------------\n")


# Exercício 8 - Função Múltiplos

print("Exercício 8)")
y = int(input("\nDigite um número a seguir: "))


def multiplos(y, soma=0):
    lista = []
    for i in range(3, y):
        if i % 3 == 0 or i % 5 == 0:
            lista.append(i)
    for i in lista:
        soma += i
    return soma


print(f"\nA soma de todos os múltiplos de 3 ou 5 abaixo de {y} resulta em {multiplos(y)}.")
print("-----------------------------------------------------------------\n")


# Exercício 9 - Função Maior

print("Exercício 9)")
lista = np.array(input("\nDigite a seguir números para compor um vetor: ").split(sep=' '), dtype=int)


def maior(lista):
    x = 0
    for i in range(len(lista)):
        if lista[i] > x:
            x = lista[i]
    return x


print(f"\nO maior valor dentre os elementos desse vetor é {maior(lista)}.")
print("-----------------------------------------------------------------\n")


# Exercício 10 - Função Menor

print("Exercício 10)")
lista = np.array(input("\nDigite a seguir números para compor um vetor: ").split(sep=' '), dtype=int)


def menor(lista):
    x = 0
    for i in range(len(lista)):
        if lista[i] < x:
            x = lista[i]
    return x


print(f"\nO menor valor dentre os elementos do vetor é {menor(lista)}.")
print("-----------------------------------------------------------------\n")


# Exercício 11 - Função Média

print("Exercício 11)")
lista = np.array(input("\nDigite a seguir números para compor um vetor: ").split(sep=' '), dtype=int)


def media(lista):
    x = 0
    for i in lista:
        x += i
    return (x / len(lista))


print(f"\nA média dos valores dos elementos do vetor é {media(lista)}.")
print("-----------------------------------------------------------------\n")


# Exercício 12 - Função Soma-Matriz

print("Exercício 12)")
x, y = input("\nDigite a seguir as dimensões da matriz: ").split(sep=' ')
matriz = []
print("Insira abaixo os elementos da matriz:\n")
for i in range(int(x)):
    lista = np.array(input().split(), dtype=int)
    matriz.append(lista)


def somaMatriz(matriz):
    soma = 0
    for array in matriz:
        for i in array:
            soma += i
    return soma


print(f"\nA soma de todos os elementos da matriz resulta em {somaMatriz(matriz)}.")
print("-----------------------------------------------------------------\n")


# Exercício 13 - Função Soma-Coluna

print("Exercício 13)")
x, y = input("\nDigite a seguir as dimensões da matriz: ").split()
matriz = []
print("Insira abaixo os elementos da matriz:\n")
for i in range(int(x)):
    lista = [int(elemento) for elemento in input().split()]
    matriz.append(lista)


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


print(f"\nA soma dos elementos da primeira coluna da transposta resulta em {somaColuna(matriz)}.")
print("-----------------------------------------------------------------\n")


# Exercício 14 - Função Soma-Diagonal

print("Exercício 14)")
x, y = input("\nDigite a seguir as dimensões da matriz: ").split()
matriz = []
print("Insira abaixo os elementos da matriz:\n")
for i in range(int(x)):
    lista = [int(elemento) for elemento in input().split()]
    matriz.append(lista)


def somaDiagonal(matriz):
    soma = 0
    for i in range(int(x)):
        soma += matriz[i][i]
    return soma


print(f"\nA soma dos elementos da diagonal principal resulta em {somaDiagonal(matriz)}.")
print("-----------------------------------------------------------------\n")


# Exercício 15 - Função Pertence

print("Exercício 15)")
vetor1 = np.array(input("\nDigite valores para compor o primeiro vetor: ").split(), dtype=int)
vetor2 = np.array(input("\nDigite valores para compor o segundo vetor: ").split(), dtype=int)


def pertence(vetor1, vetor2):
    soma = 0
    for i in vetor1:
        if i in vetor2:
            soma += i
    return soma


print(f"\nA soma dos elementos comuns entre os vetores resulta em {pertence(vetor1, vetor2)}.")
print("-----------------------------------------------------------------\n")


# Exercício 16 - Função Soma Acumulativa

print("Exercício 16)")
vetor = np.array(input("\nDigite valores para compor o vetor: ").split(), dtype=int)


def somaAcumulativa(vetor):
    soma = 0
    lista = []
    for i in vetor:
        soma += i
        lista.append(soma)
    return lista


print("\nO vetor resultante da soma acumulativa é:", end=' ')
for i in somaAcumulativa(vetor):
    print(i, end=' ')
print("\n-----------------------------------------------------------------\n")


# Exercício 17 - Função Multimat

print("Exercício 17)")
