from cArvoreBinaria import *

def main():
    print("Testing binary tree...\n")
    arvore1 = ArvoreBinaria()
    arvore1.insert(10)
    arvore1.insert(15)
    arvore1.insert(5)
    print("Imprimindo em ordem:\n")
    arvore1.displayInOrder(arvore1.getRaiz())
    print()
    arvore1.insert(13)
    arvore1.insert(7)
    arvore1.insert(4)
    arvore1.insert(20)
    arvore1.displayInOrder(arvore1.getRaiz())
    print()
    '''
    arvore1.remove(10)
    arvore1.displayInOrder(arvore1.getRaiz())
    '''
    
if __name__ == "__main__":
    main()