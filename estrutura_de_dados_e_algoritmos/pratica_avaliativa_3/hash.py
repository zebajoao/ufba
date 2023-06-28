class No:
    def __init__(self, chave=None, indice=None):
        self.chave = chave
        self.indice = indice
        self.prox = None
    
    def getChave(self):
        return self.chave
    
    def setChave(self, chave):
        self.chave = chave
        return
    
    def getIndice(self):
        return self.indice
    
    def setIndice(self, valor):
        self.indice = valor
        return
    
    def getProx(self):
        return self.prox
    
    def setProx(self, no):
        self.prox = no
        return
    
    def show(self):
        return f'{self.getChave()}'
    
class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
    
    def __call__(self):
        return self
    
    def getInicio(self):
        return self.inicio
    
    def setInicio(self, no):
        self.inicio = no
        return
    
    def getFim(self):
        return self.fim
    
    def setFim(self, no):
        self.fim = no
        return
    
    def append(self, chave):
        no = No(chave)
        if self.empty():
            self.setInicio(no)
            no.setIndice(0)
        else:
            temp = self.getFim()
            temp.setProx(no)
            no.setIndice(self.getFim().getIndice() + 1)
        self.setFim(no)
        return
    
    def display(self):
        if self.empty():
            return "Erro -> Registro vazio!"
        else:
            temp = self.getInicio()
            while temp != self.getFim():
                print(temp.show(), end=' ')
                temp = temp.getProx()
            print(temp.show())
        return
    
    def empty(self):
        if self.getInicio() == None:
            return True
        return False
    
    def newList():
        return ListaEncadeada()

class Hash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.inicio = None
        self.fim = None
        self.qtdRegistros = 0
        
    def getTamanho(self):
        return self.tamanho
    
    def setTamanho(self, valor):
        self.tamanho = valor
        return
    
    def getInicio(self):
        return self.inicio
    
    def setInicio(self, no):
        self.inicio = no
        return
    
    def getFim(self):
        return self.fim
    
    def setFim(self, no):
        self.fim = no
        return
    
    def getQtdRegistros(self):
        return self.qtdRegistros
    
    def setQtdRegistros(self, valor):
        self.qtdRegistros = valor
        return
    
    def add(self, chave):
        indice = self.hashing(chave)
        temp = self.getInicio()
        while temp.getIndice() != indice:
            temp = temp.getProx()
        lista = temp.getChave()
        lista.append(chave)
    
    def display(self, indice=None):
        if indice != None:
            no = self.find(indice)
            lista = no.getChave()
            lista.display()
            return
        else:
            no = self.getInicio()
            while no != None:
                lista = no.getChave()
                lista.display()
                no = no.getProx()
    
    def empty(self):
        if self.getQtdRegistros() == 0:
            return True
        return False
    
    def find(self, indice):
        temp = self.getInicio()
        while temp.getIndice() != indice:
            temp = temp.getProx()
        return temp
    
    def hashing(self, chave):
        k = 0
        for item in chave:
            k += (ord(item) - 96)
        return k % self.getTamanho()
    
    def newHash(tamanho):
        hash = Hash(tamanho)
        while hash.getQtdRegistros() < hash.getTamanho():
            lista = ListaEncadeada.newList()
            no = No(lista)
            if hash.empty():
                hash.setInicio(no)
                no.setIndice(0)
            else:
                temp = hash.getFim()
                temp.setProx(no)
                no.setIndice(hash.getFim().getIndice() + 1)
            hash.setFim(no)    
            hash.setQtdRegistros(hash.getQtdRegistros() + 1)
        return hash

def main():
    qtdLinhas = int(input())
    tamanho = int(input())
    indice = int(input())
    tabelaHash = Hash.newHash(tamanho)
    for i in range(qtdLinhas - 2):
        palavra = input()
        tabelaHash.add(palavra)
    tabelaHash.display(indice)

if __name__ == "__main__":
    main()