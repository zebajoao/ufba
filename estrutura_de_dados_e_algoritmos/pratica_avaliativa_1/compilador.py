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

class Pilha:
    def __init__(self):
        self.top = None 

    def getTop(self):
        return self.top
  
    def setTop(self, no):
        self.top = no 
    
    def display(self):
        if self.empty():
            print("Erro -> Pilha Vazia")
        else:
            temp = self.getTop()
            while True:
                if temp == None:
                    break
                print(temp.show(), end=' ')
                temp = temp.getProx()
    
    def empty(self):
        if self.getTop() == None:
            return True
        return False

    def push(self, chave):
        no = No(chave)
        if not self.empty():
            no.setProx(self.getTop())
        self.setTop(no)

    def pop(self):
        if self.empty():
            print("Erro -> Pilha Vazia")
        else:    
            temp = self.getTop()
            self.setTop(temp.getProx())
            temp.setProx(None)

def main():
    compilador = Pilha()
    expressao = input()
    for item in expressao:
        if item == "(" or item == "[" or item == "{":
            compilador.push(item)
        elif item == ")" or item == "]" or item == "}":
            if item == ")":
                item = "("
            elif item == "]":
                item = "["
            else:
                item = "{"
            topo = compilador.getTop()
            if (topo != None) and (topo.getChave() == item):
                compilador.pop()
            else:
                return "Invalido"
        else:
            continue 
    if compilador.empty():
        return "Valido"
    return "Invalido"

if __name__ == "__main__":
    print(main())