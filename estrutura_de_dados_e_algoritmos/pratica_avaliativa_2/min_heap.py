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
    
    def resetChildren(self):
        if self.getDir() == self:
            self.setDir(None)
        if self.getEsq() == self:
            self.setEsq(None)
        temp = self.getDir()
        self.setDir(self.getEsq())
        self.setEsq(temp)
        
    def setPointers(self, temp, no):
        if self.getDir() == temp:
            self.setDir(no)
        else:
            self.setEsq(no)
        no.setPai(self)
    
    def show(self):
        return f"{self.getChave()}"
    
class Heap:
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
        no.setPai(None)
    
    def add(self, chave):
        no = No(int(chave))
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
        self.fixUp(no)
            
    def empty(self):
        if self.getRaiz() == None:
            return True
        return False
    
    def fixUp(self, no):
        while True:
            temp = no.getPai()
            if temp == None:
                break
            elif temp.getChave() <= no.getChave():
                break
            else:
                temp2 = temp.getPai()
                if temp2 == None:
                    temp2 = No(no.getChave())
                    temp2.setDir(no.getDir())
                    temp2.setEsq(no.getEsq())
                    self.relations(temp, no)
                    temp.setDir(temp2.getDir())
                    temp.setEsq(temp2.getEsq())
                    self.root(temp, no)
                    self.setRaiz(no)
                else:
                    temp2.setPointers(temp, no)
                    self.relations(temp, no)
                    self.root(temp, no)
                    temp.resetChildren()
                temp2 = no.getNivel()
                no.setNivel(temp.getNivel())
                temp.setNivel(temp2)
                
    def inOrder(self, raiz):
        if raiz == None:
            return
        print(f"{raiz.show()}", end=' ')
        self.inOrder(raiz.getEsq())
        self.inOrder(raiz.getDir())
    
    def newHeap():    
        return Heap()
    
    def relations(self, temp, no):
        if temp.getDir() == no:
            temp.setDir(no.getEsq())
            no.setDir(temp)
            no.setEsq(temp.getEsq())
            temp.setEsq(no.getDir())
        else:
            temp.setEsq(no.getDir())
            no.setEsq(temp)
            no.setDir(temp.getDir())
            temp.setDir(no.getEsq())
        temp.setPai(no)
    
    def root(self, temp, no):
        if no.getDir() == temp:
            temp2 = no.getEsq()
        else:
            temp2 = no.getDir()
        if temp2 != None:
            temp2.setPai(no)
    
    def search(self, chave, raiz):
        if raiz == None:
            return
        if raiz.getChave() == chave:
            return raiz
        temp = self.search(chave, raiz.getEsq())
        if temp != None:
            return temp
        else:
            return self.search(chave, raiz.getDir())
    
    def selectRoot(self, raiz):
        nivelCompleto = self.verifyLevel(raiz)
        if nivelCompleto == False:
            return
        elif (raiz.getEsq() == None or raiz.getDir() == None):
            return raiz
        else:
            temp = self.selectRoot(raiz.getEsq())
            if temp != None:
                return temp
            else:
                return self.selectRoot(raiz.getDir())
    
    def verifyLevel(self, raiz):
        if self.getQtdElementos() >= ((2**(raiz.getNivel() + 1)) - 1):
            return True
        else:
            return False
        
def main():
    qtdLinhas = int(input())
    vetorDeEntrada = input().split()
    numIteracoes = int(input())
    minHeap = Heap.newHeap()
    for elemento in vetorDeEntrada:
        minHeap.add(elemento)
    minHeap.inOrder(minHeap.getRaiz())
    
if __name__=="__main__":
    main()