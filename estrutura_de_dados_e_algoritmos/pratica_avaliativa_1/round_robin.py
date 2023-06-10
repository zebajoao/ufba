class No:
    def __init__(self, chave=None, prox=None):
        self.chave = chave 
        self.prox = prox 

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
    
class Fila:
    def __init__(self):
        self.first = None
        self.last = None
    
    def getFirst(self):
        return self.first
    
    def setFirst(self, no):
        self.first = no
        
    def getLast(self):
        return self.last
    
    def setLast(self, no):
        self.last = no
    
    def display(self):
        if self.empty():
            print("Erro -> Fila vazia!")
        else:
            temp = self.getFirst()
            while True:
                if temp == None:
                    break
                print(f"{temp.show()}", end=' ')
                temp = temp.getProx()
            print()
        
    def empty(self):
        if self.getFirst() == None and self.getLast() == None:
            return True
        return False
        
    def put(self, chave):
        valor = int(chave)
        no = No(valor)
        if self.empty():
            self.setFirst(no)
            self.setLast(no)
        else:
            temp = self.getLast()
            temp.setProx(no)
            self.setLast(no)
    
    def pop(self):
        if self.empty():
            print("Erro -> Fila vazia!")
        else:
            temp = self.getFirst()
            self.setFirst(temp.getProx())
            temp.setProx(None)
            if self.getFirst() == None:
                self.setLast(None)
    
def main():
    filaIDs = Fila()
    filaUPs = Fila()
    quantum = 0
    maxUP = 0
    qtdLinhas = int(input())
    for i in range(qtdLinhas):
        linha = input().split()
        if i == 0:
            quantum = int(linha[0])
            maxUP = int(linha[1])
        else:
            for item in linha:
                if i == 1:
                    filaIDs.put(item)
                else:
                    filaUPs.put(item)
    while maxUP > 0:
        temp = filaUPs.getFirst()
        up = temp.getChave()
        for i in range(quantum):
            if up == 0 or maxUP == 0:
                break
            up -= 1
            maxUP -= 1
        filaUPs.pop()
        temp = filaIDs.getFirst()
        filaIDs.pop()
        if up > 0:
            filaUPs.put(up)
            filaIDs.put(temp.getChave())
    filaIDs.display()
    filaUPs.display()
    
if __name__ == "__main__":
    main()