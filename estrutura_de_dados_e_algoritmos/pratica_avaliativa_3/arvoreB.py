class No:
    def __init__(self, chave=None, indice=None):
        self.chave = chave
        self.indice = indice
        self.prox = None
    
    def getChave(self):
        return self.chave
    
    def setChave(self, chave):
        self.chave = chave
        return
    
    def getIndice(self):
        return self.indice
    
    def setIndice(self, valor):
        self.indice = valor
        return
    
    def getProx(self):
        return self.prox
    
    def setProx(self, no):
        self.prox = no
        return
    
    def show(self):
        return f'{self.getChave()}'
    
class ListaEncadeada:
    def __init__(self, tamanho):
        self.inicio = None
        self.fim = None
        self.qtdElementos = 0
        self.tamanho = tamanho
    
    def __call__(self):
        return self
    
    def getInicio(self):
        return self.inicio
    
    def setInicio(self, no):
        self.inicio = no
        return
    
    def getFim(self):
        return self.fim
    
    def setFim(self, no):
        self.fim = no
        return
    
    def getQtdElementos(self):
        return self.qtdElementos
    
    def setQtdElementos(self, qtdElementos):
        self.qtdElementos = qtdElementos
        return
    
    def getTamanho(self):
        return self.tamanho
    
    def setTamanho(self, tamanho):
        self.tamanho = tamanho
        return
    
    def display(self, indice):
        if self.empty():
            return "Erro -> Registro vazio!"
        else:
            temp = self.getInicio()
            while True:
                if temp == None or temp.getIndice() > indice:
                    break
                print(temp.show(), end=' ')
                temp = temp.getProx()
        return
    
    def empty(self):
        if self.getInicio() == None:
            return True
        return False
    
    def find(self, chave):
        temp = self.getInicio()
        while True:
            if temp == None or temp.getChave() == chave:
                break                
            temp = temp.getProx()
        if temp == None:
            return -1
        return temp.getIndice()
    
    def fixIndex(self, no):
        if no == self.getInicio():
            no.setIndice(0)
        aux = no
        temp = aux.getProx()
        while temp != None:
            temp.setIndice(aux.getIndice() + 1)
            aux = temp
            temp = aux.getProx()
    
    def full(self):
        if self.getQtdElementos() > self.getTamanho():
            return True
        return False
    
    def insert(self, chave, ponteiro=False, indice=-1):
        no = No(chave)
        if self.empty():
            self.setInicio(no)
            self.setFim(no)
            no.setIndice(0)
        elif not ponteiro:
            temp = self.getInicio()
            if temp.getChave() > chave:
                no.setProx(temp)
                self.setInicio(no)
                self.fixIndex(no)
            else:
                while True:
                    if temp.getProx() == None or temp.getProx().getChave() >= chave:
                        break
                    temp = temp.getProx()
                if temp.getProx() == None:
                    self.setFim(no)
                    temp.setProx(no)
                    no.setIndice(temp.getIndice() + 1)
                elif temp.getProx().getChave() == chave:
                    return
                else:
                    no.setProx(temp.getProx())
                    temp.setProx(no)
                    no.setIndice(temp.getIndice() + 1)
                    self.fixIndex(no)
        elif indice == -1:
            temp = self.getFim()
            temp.setProx(no)
            no.setIndice(temp.getIndice() + 1)
            self.setFim(no)
        else:
            temp = self.getInicio()
            for i in range(indice):
                aux = temp
                temp = temp.getProx()
            if temp == None:
                aux.setProx(no)
                no.setIndice(aux.getIndice() + 1)
                self.setFim(no)
            elif temp == self.getInicio():
                no.setProx(temp)
                no.setIndice(0)
                self.setInicio(no)
                self.fixIndex(no)
            else:
                aux.setProx(no)
                no.setProx(temp)
                no.setIndice(aux.getIndice() + 1)
                self.fixIndex(no)
        self.setQtdElementos(self.getQtdElementos() + 1)
        return
        
    def newList(tamanho):
        return ListaEncadeada(tamanho)
    
    def remove(self, chave):
        indice = self.find(chave)
        if indice == -1:
            return
        elif indice == 0:
            temp = self.getInicio()
            self.setInicio(temp.getProx())
            temp.setProx(None)
            self.setQtdElementos(self.getQtdElementos() - 1)
            self.fixIndex(self.getInicio())
            return
        else:
            temp = self.getInicio()
            for i in range(indice - 1):
                temp = temp.getProx()
            aux = temp.getProx()
            if aux == self.getFim():
                self.setFim(temp)
                temp.setProx(None)
            else:
                temp.setProx(aux.getProx())
                aux.setProx(None)
                self.fixIndex(temp)
            self.setQtdElementos(self.getQtdElementos() - 1)
            return

class PaginaB:
    def __init__(self, tamanho):
        self.chaves = ListaEncadeada.newList(tamanho)
        self.filhos = ListaEncadeada.newList(tamanho + 1)
        self.pai = None
    
    def __call__(self):
        return self
    
    def getChaves(self):
        return self.chaves
    
    def setChaves(self, lista):
        self.chaves = lista
        return
    
    def getFilhos(self):
        return self.filhos
    
    def setFilhos(self, lista):
        self.filhos = lista
        return
    
    def getPai(self):
        return self.pai
    
    def setPai(self, paginaB):
        self.pai = paginaB
        return
    
    def add(self, elemento, tipo, indice=-1):
        if tipo == "filho":
            lista = self.getFilhos()
            lista.insert(elemento, ponteiro=True, indice=indice)
        else:
            lista = self.getChaves()
            lista.insert(elemento)
        
    def full(self):
        if self.getChaves().full():
            return True
        return False
    
    def findPointer(self, chave):
        temp = self.getChaves().getInicio()
        while True:
            if temp.getProx() == None or temp.getChave() > chave:
                break
            temp = temp.getProx()
        if temp.getChave() > chave:
            return temp.getIndice()
        return (temp.getIndice() + 1)
    
class ArvoreB:
    def __init__(self, ordem):
        self.ordem = ordem
        self.raiz = None
        
    def getOrdem(self):
        return self.ordem
    
    def setOrdem(self, ordem):
        self.ordem = ordem
        return
    
    def getRaiz(self):
        return self.raiz
    
    def setRaiz(self, paginaB):
        self.raiz = paginaB
        return
    
    def newBTree(ordem):
        arvore = ArvoreB(ordem)
        raiz = PaginaB((ordem))
        arvore.setRaiz(raiz)
        return arvore
    
    def put(self, chave):
        pagina = self.selectPage(chave, self.getRaiz())
        pagina.add(chave, tipo="chave")
        if pagina.full():
            self.split(pagina)
        return
    
    def selectPage(self, chave, paginaB):
        if paginaB.getFilhos().empty():
            return paginaB
        indice = paginaB.findPointer(chave)
        temp = paginaB.getFilhos().getInicio()
        for i in range(indice):
            temp = temp.getProx()
        pagina = self.selectPage(chave, temp.getChave())
        return pagina
    
    def split(self, paginaB):
        if paginaB.getPai() == None:
            pai = PaginaB(self.getOrdem())
            self.setRaiz(pai)
            paginaB.setPai(pai)
        else:
            pai = paginaB.getPai()
            pai.getFilhos().remove(paginaB)
        menores = PaginaB(self.getOrdem())
        menores.setPai(pai)
        chaves = paginaB.getChaves()
        filhos = paginaB.getFilhos()
        temp = chaves.getInicio()
        temp2 = filhos.getInicio()
        for i in range((chaves.getQtdElementos())//2):
            menores.add(temp.getChave(), tipo="chave")
            if temp2 != None:
                menores.add(temp2.getChave(), tipo="filho")
                temp2 = temp2.getProx()
                filhos.remove(filhos.getInicio().getChave())
            temp = temp.getProx()
            chaves.remove(chaves.getInicio().getChave())
        chaves.remove(temp.getChave())
        if temp2 != None:
            filhos.remove(temp2.getChave())
            menores.add(temp2.getChave(), tipo="filho")
        pai.add(temp.getChave(), tipo="chave")
        indice = pai.findPointer(temp.getChave())
        pai.add(menores, tipo="filho", indice=(indice-1))
        pai.add(paginaB, tipo="filho", indice=indice)
        if pai.full():
            self.split(pai)

    def displaySearch(self, pagina, chave):
        indice = pagina.findPointer(chave)
        lista = pagina.getChaves()
        lista.display(indice)
        if pagina.getFilhos().empty():
            return
        temp = pagina.getFilhos().getInicio()
        for i in range(indice):
            temp = temp.getProx()
        self.displaySearch(temp.getChave(), chave)
        

def main():
    qtdLinhas = int(input())
    ordem = int(input())
    chaveDeConsulta = int(input())
    arvoreBusca = ArvoreB.newBTree(ordem)
    for i in range(qtdLinhas - 2):
        chave = int(input())
        arvoreBusca.put(chave)
    arvoreBusca.displaySearch(arvoreBusca.getRaiz(), chaveDeConsulta)
    
if __name__ == "__main__":
    main()