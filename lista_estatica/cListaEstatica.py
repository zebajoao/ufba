import numpy as np;


class listaEstatica:
    #construtor
    def __init__(self, tamanhoMaximo):
        self.max = int(tamanhoMaximo)
        self.tamanhoAtual = 0
        self.lista = np.arange(self.max)
    
    #getters and setters
    def getTamanho(self):
        return self.tamanhoAtual
    
    def setTamanho(self, tam):
        self.tamanhoAtual = tam        
    
    def getMaximo(self):
        return self.max
    
    def setMaximo(self, max):
        self.max = max
    
    #operações
    def aumentaTamanho(self):
        self.tamanhoAtual += 1
    
    def concatena(self, segundaLista):
        novoMaximo = self.getMaximo() + segundaLista.getMaximo()
        listaConcatenada = listaEstatica(novoMaximo)
        for i in range(self.getTamanho()):            
            listaConcatenada.insereValor(self.lista[i])
        for i in range(segundaLista.getTamanho()):
            listaConcatenada.insereValor(segundaLista.lista[i])
        return listaConcatenada
    
    def copia(self):
        copia = listaEstatica(self.getMaximo())
        for i in range(self.getTamanho()):
            copia.lista[i] = self.lista[i]
            copia.aumentaTamanho()
        return copia
    
    def encontraElemento(self, indice):
        if self.listaVazia():
            string = "erro -> lista vazia\n"
            string += f"Quantidade de elementos armazenados: {self.getTamanho()}."
            return string
        elif indice < 0 or indice >= self.getTamanho():
            return "erro -> índice inexistente\n"
        else:
            return self.lista[indice]
    
    def encontraIndice(self, valor):
        if self.listaVazia():
            string = "erro -> lista vazia\n"
            string += f"Quantidade de elementos armazenados: {self.getTamanho()}."
            return string
        else:
            for i in range(self.getTamanho()):
                if self.lista[i] == valor:
                    return i
            return "erro -> item não encontrado\n"
    
    def encontraMaior(self):
        i = 0
        maior = self.lista[0]
        while i < self.getTamanho():
            if self.lista[i] > maior:
                maior = self.lista[i]
            i += 1
        return maior
    
    def encontraMenor(self):
        i = 0
        menor = self.lista[0]
        while i < self.getTamanho():
            if self.lista[i] < menor:
                menor = self.lista[i]
            i += 1
        return menor
    
    def imprime(self):
        if self.listaVazia():
            string = "erro -> lista vazia\n"
            string += f"Quantidade de elementos armazenados: {self.getTamanho()}."
            return string
        else:
            string = '['
            for i in range(self.getTamanho() - 1):
                string += f"{self.lista[i]}, "
            string += f"{self.lista[i + 1]}]"
            return string

    def imprimeCrescente(self):
        if self.listaVazia():
            string = "erro -> lista vazia\n"
            string += f"Quantidade de elementos armazenados: {self.getTamanho()}."
            return string
        else:
            string = '['
            menor = self.encontraMenor() - 1
            for i in range(self.getTamanho()):
                temp = self.encontraMaior()
                j = 0
                while j < self.getTamanho():
                    if self.lista[j] < temp and self.lista[j] > menor:
                        temp = self.lista[j]
                    j += 1
                menor = temp
                if i < self.getTamanho() - 1:
                    string += f"{menor}, "
                else:
                    string += f"{menor}]"
            return string
            
            '''
            * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
            *                         Implementação Alternativa                         *
            * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
            * a = listaEstatica(self.getMaximo())                                      *
            * for i in range(self.getTamanho()):                                        *
            *     menor = self.encontraMaior()                                          *
            *     j = 0                                                                 *
            *     while j < self.getTamanho():                                          *
            *         if self.lista[j] < menor and not a.possuiElemento(self.lista[j]): *
            *             menor = self.lista[j]                                         *
            *         j += 1                                                            *
            *     a.insereValor(menor)                                                  *
            * a.imprime()                                                               *
            * del a                                                                     *
            * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
            '''
            
    def imprimeDecrescente(self):
        if self.listaVazia():
            string = "erro -> lista vazia\n"
            string += f"Quantidade de elementos armazenados: {self.getTamanho()}.\n"
            return string
        else:
            string = '['
            maior = self.encontraMaior() + 1
            for i in range(self.getTamanho()):
                temp = self.encontraMenor()
                j = 0
                while j < self.getTamanho():
                    if self.lista[j] > temp and self.lista[j] < maior:
                        temp = self.lista[j]
                    j += 1
                maior = temp
                if i < self.getTamanho() - 1:
                    string += f"{maior}, "
                else:
                    string += f"{maior}]"
            return string
                    
            '''
            * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
            *                         Implementação Alternativa                         *
            * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 
            * a = listaEstatica(self.getMaximo())                                      *
            * for i in range(self.getTamanho()):                                        *
            *     maior = self.encontraMenor()                                          *
            *     j = 0                                                                 *
            *     while j < self.getTamanho():                                          *
            *         if self.lista[j] > maior and not a.possuiElemento(self.lista[j]): *
            *             maior = self.lista[j]                                         *
            *         j += 1                                                            *
            *     a.insereValor(maior)                                                  *
            * a.imprime()                                                               *
            * del a                                                                     *
            * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
            '''
    
    def insereValor(self, elemento, posicao = None):
        if posicao == None or self.listaVazia():
            indice = self.getTamanho()
        else:
            indice = posicao
        if self.listaCheia():
            print("erro -> lista cheia\n")
            print(f"Quantidade de elementos armazenados: {self.getTamanho()}.")
            print(f"Máximo suportado: {self.getMaximo()}.\n")
        elif indice == self.getTamanho():
            self.lista[indice] = elemento
            self.aumentaTamanho()
        else:
            for i in range(self.getTamanho(), indice, -1):
                self.lista[i] = self.lista[i-1]
            self.lista[indice] = elemento
            self.aumentaTamanho()
    
    def limpar(self):
        self.setTamanho(0)
    
    def listaCheia(self):
        if self.getTamanho() == self.getMaximo():
            return 1
        else:
            return 0
        
    def listaVazia(self):
        if self.getTamanho() == 0:
            return 1
        else:
            return 0
    
    def possuiElemento(self, elemento):
        for i in range(self.getTamanho()):
            if self.lista[i] != elemento:
                continue
            else:
                return 1
        return 0
    
    def removeOcorrencias(self, valor):
        for i in range(self.getTamanho()):
            if self.lista[i] == valor:
                if i == self.getTamanho() - 1:
                    self.setTamanho(i)
                else:
                    k = i
                    j = k + 1
                    while j < self.getTamanho():
                        self.lista[k] = self.lista[j]
                        k += 1
                        j += 1
                    novoTamanho = self.getTamanho() - 1
                    self.setTamanho(novoTamanho)

