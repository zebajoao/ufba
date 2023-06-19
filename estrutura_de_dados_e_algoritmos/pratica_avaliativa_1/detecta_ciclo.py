class No:
    def __init__(self, chave=None, prox=None):
        self.chave = chave
        self.prox = prox
    
    def getChave(self):
        return self.chave
    
    def setChave(self, chave):
        self.chave = chave
    
    def getProx(self):
        return self.prox
    
    def setProx(self, no):
        self.prox = no
    
class ListaEncadeadaSimples:
    def __init__(self):
        self.head = None
    
    def getHead(self):
        return self.head

    def setHead(self, no):
        self.head = no

    def append(self, chave):
        no = No(chave)
        if self.getHead() == None:
            self.setHead(no)
        else:
            temp = self.getHead()
            while temp.getProx() != None:
                temp = temp.getProx()
            temp.setProx(no)
            
    def detectsCycle(self):
        temp1 = self.getHead()
        temp2 = temp1.getProx()
        while temp2 != None:
            if temp1 == temp2:
                return "Ciclo"
            temp1 = temp1.getProx()
            temp2 = temp2.getProx()
            if temp2 != None:
                temp2 = temp2.getProx()
        return "Sem Ciclo"
        
    def search(self, chave):
        temp = self.getHead()
        while temp != None:
            if temp.getChave() == chave:
                return temp
            temp = temp.getProx() 

def main():
    lista = ListaEncadeadaSimples()
    qtdLinhas = int(input())
    for i in range(qtdLinhas - 1):
        if i == 0:
            chaves = input().split()
            for item in chaves:
                lista.append(item)
        no = input().split()
        elemento = lista.search(no[0])
        proximo = lista.search(no[1])
        elemento.setProx(proximo)
    print(lista.detectsCycle())
            
if __name__ == "__main__":
    main()