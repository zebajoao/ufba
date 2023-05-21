class No:
    def __init__(self, info=None, prox=None):
        self.info = info
        self.proximo = prox
        
    def getInfo(self):
        return self.info

    def setInfo(self, info):
        self.info = info
        
    def getProximo(self):
        return self.proximo
    
    def setProximo(self, no):
        self.proximo = no
    