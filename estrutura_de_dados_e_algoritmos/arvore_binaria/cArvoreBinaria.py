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
    
    
    