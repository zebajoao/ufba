class No:
    def __init__(self, chave, no):
        self.chave = chave
        self.prox = no
    
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
    
    