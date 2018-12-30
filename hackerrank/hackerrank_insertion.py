class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

def preOrder(root):
    if root == None:
        return
    print root.info,
    preOrder(root.left)
    preOrder(root.right)

class BinarySearchTree:
    def __init__(self):
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self.insert_node(val,self.root)

    def insert_node(self,val,node):
        if val < node.info:
            if node.left:
                self.insert_node(val,node.left)
            else:
                node.left = Node(val)
        else:
            if node.right:
                self.insert_node(val,node.right)
            else:
                node.right = Node(val)


tree = BinarySearchTree()
t = int(raw_input())

arr = list(map(int, raw_input().split()))

for i in xrange(t):
    tree.insert(arr[i])

preOrder(tree.root)
