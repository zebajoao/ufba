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
        
    def show(self):
        return f"{self.getChave()}"
        
class ArvoreBinaria:
    def __init__(self):
        self.profundidade = 0
        self.qtdElementos = 0
        self.raiz = None
        
    def getProfundidade(self):
        return self.profundidade
    
    def setProfundidade(self, valor):
        self.profundidade = valor
    
    def getQtdElementos(self):
        return self.qtdElementos
    
    def setQtdElementos(self, valor):
        self.qtdElementos = valor
    
    def getRaiz(self):
        return self.raiz
    
    def setRaiz(self, no):
        self.raiz = no
    
    def add(self, elemento):
        no = No(elemento)
        if self.empty():
            self.setRaiz(no)
        else:
            raiz = self.selectRoot(self.getRaiz())
            if raiz.getEsq() == None:
                raiz.setEsq(no)
            else:
                raiz.setDir(no)
            self.setProfundidade((raiz.getNivel() + 1))
            no.setPai(raiz)
        self.setQtdElementos(self.getQtdElementos() + 1)
        no.setNivel(self.getProfundidade())

    def display(self, raiz):
        if raiz == None:
            return
        print(f"{raiz.show()}", end=' ')
        self.display(raiz.getEsq())
        self.display(raiz.getDir())
            
    def empty(self):
        if self.getRaiz() == None:
            return True
        return False
    
    def newTree():    
        return ArvoreBinaria()
    
    def selectRoot(self, raiz):
        nivelCompleto = self.verifyLevel(raiz)
        if nivelCompleto == False:
            return
        elif (raiz.getEsq() == None or raiz.getDir() == None):
            return raiz
        else:
            raiz = self.selectRoot(raiz.getEsq())
            if raiz != None:
                return raiz
            else:
                return self.selectRoot(raiz.getDir())
    
    def verifyLevel(self, raiz):
        if self.getQtdElementos() >= ((2**(raiz.getNivel() + 1)) - 1):
            return True
        else:
            return False
            
def main():
    print("Iniciando teste")
    arvore = ArvoreBinaria.newTree()
    arvore.add(1)
    arvore.add(2)
    arvore.add(3)
    arvore.add(4)
    arvore.add(5)
    arvore.display(arvore.getRaiz())
    print(f"\nProfundidade: {arvore.getProfundidade()}.")
    
if __name__ == "__main__":
    main()