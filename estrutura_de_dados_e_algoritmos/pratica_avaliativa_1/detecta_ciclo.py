class No:
    def __init__(self, chave, prox):
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
        
    def show(self):
        return f"{self.getChave()}"
    
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
            while temp.prox != None:
                temp = temp.prox
            temp.prox = no
        
    def search(self, chave):
        temp = self.getHead()
        while temp != None:
            if temp.valor == chave:
                return temp
            temp = temp.prox 
