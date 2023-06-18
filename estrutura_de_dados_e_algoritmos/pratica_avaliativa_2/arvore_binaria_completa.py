class No:
    def __init__(self, chave=None, nivel=None, pai=None, esq=None, dir=None):
        self.chave = chave
        self.nivel = nivel
        self.pai = pai
        self.esq = esq
        self.dir = dir
          
    def getChave(self):
        return self.chave
    
    def setChave(self, chave):
        self.chave = chave
        
    def getNivel(self):
        return self.nivel
    
    def setNivel(self, nivel):
        self.nivel = nivel
        
    def getPai(self):
        return self.pai
    
    def setPai(self, no):
        self.pai = no
        
    def getEsq(self):
        return self.esq
    
    def setEsq(self, no):
        self.esq = no
        
    def getDir(self):
        return self.dir
    
    def setDir(self, no):
        self.dir = no
        
class ArvoreBinaria:
    def __init__(self, profundidade=None):
        self.raiz = None
        self.profundidade = profundidade
    
    def getRaiz(self):
        return self.raiz
    
    def setRaiz(self, no):
        self.raiz = no
        
    def getProfundidade(self):
        return self.profundidade
    
    def setProfundidade(self, valor):
        self.profundidade = valor
    
    def add(self, elemento):
        no = No(elemento)
        if self.empty():
            self.setRaiz(no)
            self.setProfundidade(0)
            no.setNivel(self.getProfundidade())
        else:
            raiz = self.selectRoot(self.getRaiz())
            if raiz.getEsq() == None:
                raiz.setEsq(no)
            else:
                raiz.setDir(no)
            self.setProfundidade((raiz.getNivel() + 1))
            no.setPai(raiz)
            no.setNivel(self.getProfundidade())
            
    def selectRoot(self, raiz):
        nivelCompleto = self.verifyLevel(raiz.getNivel(), raiz)
        if nivelCompleto != True:
            return
        elif (raiz.getEsq() == None or raiz.getDir() == None):
            return raiz
        else:
            self.selectRoot(raiz.getEsq())
            self.selectRoot(raiz.getDir())
            
        
    def empty(self):
        if self.getRaiz() == None:
            return True
        return False
    
    def newTree():    
        return ArvoreBinaria()
    
    def verifyLevel(self, nivel, raiz, qtdElementos=0):
        if raiz == None:
            return
        elif raiz.getNivel() == nivel:
            qtdElementos += 1
            if qtdElementos == (2**(raiz.getNivel())):
                return True
            return
        else:
            self.verifyLevel(nivel, raiz.getEsq(), qtdElementos)
            self.verifyLevel(nivel, raiz.getDir(), qtdElementos)