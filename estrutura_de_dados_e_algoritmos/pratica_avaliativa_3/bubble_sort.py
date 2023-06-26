class No:
    def __init__(self, chave=None, antr=None, prox=None):
        self.chave = chave
        self.antr = antr
        self.prox = prox
        
    def getChave(self):
        return self.chave
    
    def setChave(self, chave):
        self.chave = chave
        return
    
    def getAntr(self):
        return self.antr
    
    def setAntr(self, no):
        self.antr = no
        return
    
    def getProx(self):
        return self.prox
    
    def setProx(self, no):
        self.prox = no
        return
    
    def show(self):
        return f"{self.getChave()}"
    
class Vetor:
    def __init__(self, tam):
        self.tamanho = tam
        self.qtdElementos = 0
        self.inicio = None
        self.fim = None
    
    def getTamanho(self):
        return self.tamanho
    
    def getQtdElementos(self):
        return self.qtdElementos
    
    def setQtdElementos(self, valor):
        self.qtdElementos = valor
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
    
    def append(self, chave):
        no = No(chave)
        if self.empty():
            self.setInicio(no)
        elif self.full():
            return "Erro -> vetor cheio!"
        else:
            temp = self.getFim()
            temp.setProx(no)
            no.setAntr(temp)
        self.setFim(no)
        self.setQtdElementos(self.getQtdElementos() + 1)
        return
    
    def display(self):
        if self.empty():
            return "Erro -> vetor vazio!"
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
    
    def full(self):
        if self.getQtdElementos() == self.getTamanho():
            return True
        return False
    
    def remove(self, chave):
        if self.empty():
            return "Erro -> vetor vazio!"
        no = self.search(chave)
        if no == None:
            return "Erro -> elemento não encontrado!"
        elif no == self.getInicio():
            self.setInicio(no.getProx())
        elif no == self.getFim():
            temp = no.getAntr()
            temp.setProx(None)
            self.setFim(temp)
        else:
            temp = self.getInicio()
            while temp.getProx() != no:
                temp = temp.getProx()
            temp.setProx(no.getProx())
        no.setProx(None)
        self.setQtdElementos(self.getQtdElementos() - 1)
        return
    
    def resetInicio(self):
        temp = self.getFim()
        while temp.getAntr() != None:
            temp = temp.getAntr()
        self.setInicio(temp)
        return
        
    def search(self, chave):
        no = No(chave)
        temp = self.getInicio()
        while True:
            if temp == None:
                return
            elif temp == no:
                return temp
            else:
                temp = temp.getProx()
                
    def switchKeys(self, no1, no2):
        temp = no1.getChave()
        no1.setChave(no2.getChave())
        no2.setChave(temp)
        return

def bubbleSort(vetor, limite):
    temp = vetor.getFim()
    for i in range(limite):
        temp2 = vetor.getInicio()
        while temp2 != temp:
            if temp2.getChave() > temp2.getProx().getChave():
                vetor.switchKeys(temp2, temp2.getProx())
            temp2 = temp2.getProx()
        temp = temp.getAntr()

def main():
    qtdLinhas = int(input())
    vetor = Vetor(qtdLinhas - 1)
    maxIteracoes = int(input())
    for i in range(qtdLinhas - 1):
        chave = int(input())
        vetor.append(chave)
    bubbleSort(vetor, maxIteracoes)
    vetor.display()
    
if __name__ == "__main__":
    main()