class No:

    def __init__(self, valor=None, prox=None, anter=None):
        self.valor = valor
        self.proximo = prox
        self.anterior = anter
        
    def getValor(self):
        return self.valor

    def setValor(self, valor):
        self.valor = valor
        
    def getProximo(self):
        return self.proximo
    
    def setProximo(self, no):
        self.proximo = no
        
    def getAnterior(self):
        return self.anterior
    
    def setAnterior(self, no):
        self.anterior = no