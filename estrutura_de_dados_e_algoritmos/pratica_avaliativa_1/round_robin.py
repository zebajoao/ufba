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
        
    def show(self):
        return f"{self.getChave()}"
    
class Fila:
    def __init__(self):
        self.first = None
        self.last = None
    
    def getFirst(self):
        return self.first
    
    def setFirst(self, no):
        self.first = no
        
    def getLast(self):
        return self.last
    
    def setLast(self, no):
        self.last = no
        
    def empty(self):
        if self.getFirst() == None and self.getLast() == None:
            return True
        return False
        
    def put(self, chave):
        no = No(chave)
        if self.empty():
            self.setFirst(no)
            self.setLast(no)
        else:
            temp = self.getLast()
            temp.setProx(no)
            self.setLast(no)
    
    def pop(self):
        if self.empty():
            print("Erro -> Fila vazia!")
        else:
            temp = self.getFirst()
            self.setFirst(temp.getProx())
            temp.setProx(None)
    