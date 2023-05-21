def fibonacci(x, soma=0, i=2):
    lista = [0, 1]
    while i <= x:
        soma = lista[i-2] + lista[i-1]
        lista.append(soma)
        i += 1
    return soma


x = int(input())
print(fibonacci(x))