from cNo import *

class ArvoreBinaria:
    def __init__(self):
        self.root = None
        
    def getRoot(self):
        return self.root
    
    def setRoot(self, node):
        self.root = node
        
    def displayInOrder(self, root):
        if root == None:
            return
        self.displayInOrder(root.getLeftChild)
        print(root.show)
        self.displayInOrder(root.getRightChild)
        
    def empty(self):
        if self.getRoot == None:
            return 1
        return 0
    
    def insert(self, key):
        element = No(key)
        if self.empty:
            self.setRoot(element)
        else:
            temp = self.getRoot
            while True:
                if element.getKey <= temp.getKey:
                    if temp.getLeftChild == None:
                        element.setFather(temp)
                        temp.setLeftChild(element)
                        break
                    temp = temp.getLeftChild
                    continue
                else:
                    if temp.getRightChild == None:
                        element.setFather(temp)
                        temp.setRightChild(element)
                        break
                    temp = temp.getRightChild
                    continue
    
    