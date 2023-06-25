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
    
    def compareChildren(self):
        esq = self.getEsq()
        dir = self.getDir()
        if esq == None:
            return dir
        elif dir == None:
            return esq
        elif esq.getChave() < dir.getChave():
            return esq
        else:
            return dir
    
    '''
    def resetChildren(self, inversor=False):
        if self.getDir() == self:
            self.setDir(None)
        if self.getEsq() == self:
            self.setEsq(None)
        if inversor:
            temp = self.getDir()
            self.setDir(self.getEsq())
            self.setEsq(temp)
        
    def setPointers(self, temp, no):
        if self.getDir() == temp:
            self.setDir(no)
        else:
            self.setEsq(no)
        no.setPai(self)
    '''
    
    def show(self):
        return f"{self.getChave()}"
    
class Heap:
    def __init__(self):
        self.profundidade = 0
        self.qtdElementos = 0
        self.raiz = None
        self.ultimaFolha = None
        
    def getProfundidade(self):
        return self.profundidade
    
    def setProfundidade(self, valor=None):
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
        
    def getUltimaFolha(self):
        return self.ultimaFolha
    
    def setUltimaFolha(self, no):
        if no == None:
            return
        if no.getNivel() == self.getProfundidade():
            self.ultimaFolha = no
        if no.getEsq() != None:
            self.setUltimaFolha(no.getEsq())
        self.setUltimaFolha(no.getDir())
            
    def add(self, chave):
        no = No(int(chave))
        if self.empty():
            self.setRaiz(no)
            self.setUltimaFolha(no)
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
        self.setUltimaFolha(no)
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
                aux = no.getChave()
                no.setChave(temp.getChave())
                temp.setChave(aux)
            no = temp
    
    def fixDown(self, no):
        while True:
            temp = no.compareChildren()
            if temp == None:
                break
            elif temp.getChave() >= no.getChave():
                break
            else:
                aux = no.getChave()
                no.setChave(temp.getChave())
                temp.setChave(aux)
            no = temp
    
    '''
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
                    self.relationsUp(temp, no)
                    temp.setDir(temp2.getDir())
                    temp.setEsq(temp2.getEsq())
                    self.root(temp, no)
                    temp.resetChildren()
                    self.root(temp.getEsq(), temp)
                    self.root(temp.getDir(), temp)
                    self.setRaiz(no)
                else:
                    temp2.setPointers(temp, no)
                    self.relationsUp(temp, no)
                    self.root(temp, no)
                    temp.resetChildren(inversor=True)
                    self.root(temp.getEsq(), temp)
                    self.root(temp.getDir(), temp)
                temp2 = no.getNivel()
                no.setNivel(temp.getNivel())
                temp.setNivel(temp2)
                self.setUltimaFolha(temp)
                
    def fixDown(self, no):
        while True:
            temp = no.compareChildren()
            if temp == None:
                break
            elif temp.getChave() > no.getChave():
                break
            else:
                temp2 = no.getPai()
                if temp2 == None:
                    temp2 = No(temp.getChave())
                    temp2.setDir(temp.getDir())
                    temp2.setEsq(temp.getEsq())
                    self.relationsDown(no, temp)
                    no.setDir(temp2.getDir())
                    no.setEsq(temp2.getEsq())
                    self.root(no, temp)
                    no.resetChildren()
                    self.root(no.getEsq(), no)
                    self.root(no.getDir(), no)
                    self.setRaiz(temp)
                else:
                    temp2.setPointers(no, temp)
                    self.relationsDown(no, temp)
                    self.root(no, temp)
                    no.resetChildren()
                    self.root(no.getEsq(), no)
                    self.root(no.getDir(), no)
                temp2 = temp.getNivel()
                temp.setNivel(no.getNivel())
                no.setNivel(temp2)
    '''
    
    
    def min(self):
        return self.getRaiz().getChave()
    
    def newHeap():    
        return Heap()
    
    def preOrder(self, raiz):
        if raiz == None:
            return
        print(f"{raiz.show()}", end=' ')
        self.preOrder(raiz.getEsq())
        self.preOrder(raiz.getDir())
    
    '''
    def relationsUp(self, temp, no):
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
    
    def relationsDown(self, no, temp):
        if no.getEsq() == temp:
            no.setEsq(temp.getEsq())
            temp.setEsq(no.getDir())
            no.setDir(temp.getDir())
            temp.setDir(temp.getEsq())
            temp.setEsq(no)
        else:
            no.setDir(temp.getDir())
            temp.setDir(no.getEsq())
            no.setEsq(temp.getEsq())
            temp.setEsq(temp.getDir())
            temp.setDir(no)
        no.setPai(temp)
    '''
    
    def remove(self, chave):
        no = self.search(int(chave), self.getRaiz())
        folha = self.getUltimaFolha()
        temp = folha.getPai()
        if folha == temp.getDir():
            temp.setDir(None)
        else:
            temp.setEsq(None)
        folha.setPai(no.getPai())
        folha.setEsq(no.getEsq())
        folha.setDir(no.getDir())
        folha.setNivel(no.getNivel())
        temp = no.getPai()
        if temp == None:
            self.setRaiz(folha)
        elif temp.getEsq() == no:
            temp.setEsq(folha)
        else:
            temp.setDir(folha)
        no.setPai(None)
        no.setEsq(None)
        no.setDir(None)
        self.setQtdElementos(self.getQtdElementos() - 1)
        self.updateDepth()
        self.fixDown(folha)
        self.setUltimaFolha(self.getRaiz())
        
    '''
    def root(self, temp, no):
        if no.getDir() == temp:
            temp2 = no.getEsq()
        else:
            temp2 = no.getDir()
        if temp2 != None:
            temp2.setPai(no)
    '''
    
    def search(self, chave, raiz):
        if raiz == None:
            return
        if raiz.getChave() == chave:
            return raiz
        temp = self.search(chave, raiz.getEsq())
        if temp != None:
            return temp
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
            return self.selectRoot(raiz.getDir())
    
    def updateDepth(self):
        temp = self.getRaiz()
        while temp.getEsq() != None:
            temp = temp.getEsq()
        self.setProfundidade(temp.getNivel())
    
    def verifyLevel(self, raiz):
        if self.getQtdElementos() >= ((2**(raiz.getNivel() + 1)) - 1):
            return True
        else:
            return False
        
class Vetor:
    def __init__(self, tam):
        self.inicio = None
        self.fim = None
        self.tamanho = tam
        self.qtdElementos = 0
    
    def getInicio(self):
        return self.inicio
    
    def setInicio(self, no):
        self.inicio = no
        
    def getFim(self):
        return self.fim
    
    def setFim(self, no):
        self.fim = no
        
    def getTam(self):
        return self.tamanho
    
    def setTam(self, valor):
        self.tamanho = valor
    
    def getQtdElementos(self):
        return self.qtdElementos
    
    def setQtdElementos(self, valor):
        self.qtdElementos = valor
        
    def append(self, chave):
        no = No(int(chave))
        if self.empty():
            self.setInicio(no)
            self.setFim(no)
            self.setQtdElementos(self.getQtdElementos() + 1)
        elif self.full():
            print("Erro -> Vetor cheio!")
        else:
            temp = self.getFim()
            temp.setDir(no)
            no.setEsq(temp)
            self.setFim(no)
            self.setQtdElementos(self.getQtdElementos() + 1)
    
    def display(self):
        if self.empty():
            print("Erro -> Vetor vazio!")
        else:
            temp = self.getInicio()
            while True:
                if temp == None:
                    break
                print(temp.show(), end=' ')
                temp = temp.getDir()
            
    def empty(self):
        if self.getQtdElementos() == 0:
            return True
        return False
    
    def full(self):
        if self.getQtdElementos() == self.getTam():
            return True
        return False
        
def main():
    qtdLinhas = int(input())
    vetorDeEntrada = input().split()
    numIteracoes = int(input())
    minHeap = Heap.newHeap()
    for elemento in vetorDeEntrada:
        minHeap.add(elemento)
    vetor = Vetor(numIteracoes)
    for i in range(numIteracoes):
        elemento = minHeap.min()
        minHeap.remove(elemento)
        vetor.append(elemento)
        minHeap.preOrder(minHeap.getRaiz())
        print()
    vetor.display()
    
if __name__=="__main__":
    main()