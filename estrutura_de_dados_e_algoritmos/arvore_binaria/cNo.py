class No:
    def __init__(self, key=None, father=None, leftChild=None, rightChild=None):
        self.key = key
        self.father = father
        self.left = leftChild
        self.right = rightChild
        
    def getKey(self):
        return self.key
    
    def setKey(self, value):
        self.key = value
        
    def getFather(self):
        return self.father
    
    def setFather(self, node):
        self.father = node
        
    def getLeftChild(self):
        return self.left
    
    def setLeftChild(self, node):
        self.left = node
        
    def getRightChild(self):
        return self.right
    
    def setRIghtChild(self, node):
        self.right = node
        
    def show(self):
        return f"{self.getKey}"
    