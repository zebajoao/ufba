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
    
class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
    
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
        else:
            temp = self.getFim()
            temp.setProx(no)
            no.setAntr(temp)
        self.setFim(no)
        return
    
    def concatenate(self, vetor):
        if vetor.empty():
            return
        if self.empty():
            self.setInicio(vetor.getInicio())
            self.setFim(vetor.getFim())
            return
        temp = self.getFim()
        temp.setProx(vetor.getInicio())
        temp = vetor.getInicio()
        temp.setAntr(self.getFim())
        self.setFim(vetor.getFim())
        return
    
    def display(self):
        if self.empty():
            return "Erro -> lista vazia!"
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
    
    def remove(self, chave):
        if self.empty():
            return "Erro -> lista vazia!"
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

def quickSort(lista, pivot, i=0):
    menores = Lista()
    maiores = Lista()
    temp = lista.getInicio()
    while temp != None:
        if temp.getChave() < pivot:
            menores.append(temp.getChave())
        if temp.getChave() > pivot:
            maiores.append(temp.getChave())
        temp = temp.getProx()
    iteracao = i
    if iteracao == 0:
        if menores.empty() and maiores.empty():
            return pivot
        elif menores.empty():
            temp = pivot
            temp2 = maiores.getInicio().getChave()
        elif maiores.empty():
            temp = menores.getInicio().getChave()
            temp2 = pivot
        else:
            temp = menores.getInicio().getChave()
            temp2 = maiores.getInicio().getChave()
        print(temp, temp2, end=' ')
    iteracao += 1
    if not menores.empty():
        menores = quickSort(menores, menores.getInicio().getChave(), iteracao)
    if not maiores.empty():
        maiores = quickSort(maiores, maiores.getInicio().getChave(), iteracao)
    listaAuxiliar = menores
    listaAuxiliar.append(pivot)
    listaAuxiliar.concatenate(maiores)
    return listaAuxiliar
    

def main():
    qtdLinhas = int(input())
    pivot = int(input())
    lista = Lista()
    for i in range(qtdLinhas - 1):
        chave = int(input())
        lista.append(chave)
    lista = quickSort(lista, pivot)
    lista.display()
    
if __name__ == "__main__":
    main()