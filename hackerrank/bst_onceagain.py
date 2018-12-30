class Node:
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


class BinearySearchTree:
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
        if self.root:
            return self.getMin(self.root)

    def getMin(self,node):
        if node.leftchild:
            return self.getMin(node.leftchild)

        return node.data

    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)


    def getMax(self,node):
        if node.rightchild:
            return self.getMax(node.rightchild)

        return node.data

    def traverse(self):
        if self.root:
            self.traverseInorder(self.root)

    def traverseInorder(self,node):
        if node.leftchild:
            self.traverseInorder(node.leftchild)

        print node.data

        if node.rightchild:
            self.traverseInorder(node.rightchild)

    def traverserPreOrder(self,node):
        if self.root:
            print node.data
            if node.leftchild:
                self.traverserPreOrder(node.leftchild)
            if node.rightchild:
                self.traverserPreOrder(node.rightchild)

    def height(self):
        return self.get_height(self.root)

    def get_height(self,root):
        if root == None:
            return 0
        lh = self.get_height(root.leftchild)
        rh = self.get_height(root.rightchild)
        print 'this is left {}'.format(lh)
        print 'this is right {}'.format(rh)
        if lh>rh:
            lh = lh+1
        else:
            rh = rh+1


bst = BinearySearchTree()
bst.insert(3)
bst.insert(2)
bst.insert(1)
bst.insert(5)
bst.insert(4)
bst.insert(6)
bst.insert(7)
print bst.height()
