class No:
    def __init__(self, valor=None, prox=None):
        self.valor = valor
        self.proximo = prox
        
    def getValor(self):
        return self.valor
    
    def setValor(self, valor):
        self.valor = valor
        
    def getProximo(self):
        return self.proximo
    
    def setProximo(self, no):
        self.proximo = no