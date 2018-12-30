class Node():
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


class BinearySearchTree():
    def __init__(self):
        self.root = None

    def insert(self,data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data,self.root)

    def insertNode(self,data,node):
        if data < node.data:
            if node.leftchild:
                self.insertNode(data,node.leftchild)
            else:
                node.leftchild = Node(data)
        else:
            if node.rightchild:
                self.insertNode(data,node.rightchild)
            else:
                node.rightchild = Node(data)

    def getMinValue(self):
        if not self.root:
            return self.getMinValue(self.root)

    def getMin(self,node):
        if node.leftchild:
            return self.getMin(node.leftchild)

        return node.data

    def getMaxValue(self):
        if self.root:
            return self.getMaxValue(self.root)


    def getMax(self,node):
        if node.rightchild:
            return self.getMax(node.rightchild)

        return node.data

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self,node):
        if node.leftchild:
            self.traverseInOrder(node.leftchild)

        print node.data

        if node.rightchild:
            self.traverseInOrder(node.rightchild)


if __name__ == "__main__":
    bst = BinearySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(6)
    print bst.getMinValue()
