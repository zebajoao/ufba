class No:
    def __init__(self, chave=None, pai=None, esq=None, dir=None):
        self.chave = chave
        self.pai = pai
        self.esq = esq
        self.dir = dir
          
    def getChave(self):
        return self.chave
    
    def setChave(self, chave):
        self.chave = chave
           
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
        self.raiz = None
    
    def getRaiz(self):
        return self.raiz
    
    def setRaiz(self, no):
        self.raiz = no
    
    def add(self, chave):
        no = No(chave)
        if self.empty():
            self.setRaiz(no)
        else:
            temp = self.getRaiz()
            while True:
                if no.getChave() < temp.getChave():
                    if temp.getEsq() == None:
                        no.setPai(temp)
                        temp.setEsq(no)
                        break
                    temp = temp.getEsq()
                    continue
                else:
                    if temp.getDir() == None:
                        no.setPai(temp)
                        temp.setDir(no)
                        break
                    temp = temp.getDir()
                    continue

    def clearTree(self):
        self.setRaiz(None)
    
    def inOrder(self, chave, raiz):
        if raiz == None:
            return
        self.inOrder(chave, raiz.getEsq())
        print(f"{raiz.show()}", end=' ')
        if raiz.getChave() == chave:
            return
        self.inOrder(chave, raiz.getDir())
            
    def empty(self):
        if self.getRaiz() == None:
            return True
        return False
    
    def newTree():    
        return ArvoreBinaria()
    
    def search(self, chave, raiz):
        if raiz == None:
            return
        temp = self.search(chave, raiz.getEsq())
        if temp != None:
            return temp
        elif raiz.getChave() == chave:
            return raiz
        else:
            return self.search(chave, raiz.getDir())

def main():
    qtdLinhas = int(input())
    arvore = ArvoreBinaria.newTree()
    vetorDeEntrada = input().split()
    for elemento in vetorDeEntrada:
        arvore.add(int(elemento))
    #inserir valores para remoção
    valorParaPesquisa = int(input())
    arvore.inOrder(valorParaPesquisa, arvore.getRaiz())
        
if __name__ == "__main__":
    main()