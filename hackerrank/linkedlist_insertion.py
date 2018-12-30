class Node:

    def __init__(self,data):
        self.data = data
        self.nextnode = None




class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    # o(1) at the inserting at the start
    def insertStart(self,data):

        self.size = self.size + 1

        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextnode = self.head
            self.head = newNode

    # o(N) time complexity
    def insertEnd(self,data):

        self.size = self.size + 1
        newNode = Node(data)

        actualNode = self.head
        while actualNode.nextnode is not None:
            actualNode = actualNode.nextnode

        actualNode.nextnode = newNode



    def traverseList(self):

        actualNode = self.head

        while actualNode is not None:
            print actualNode.data
            actualNode = actualNode.nextnode

    def sizeoflist(self):
        return self.size


    def remove(self,data):
        if self.head is None:
            return

        self.size = self.size -1
        currentNode = self.head
        previousNode = None

        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextnode

        if previousNode is None:
            self.head = currentNode.nextnode
        else:
            previousNode.nextnode = currentNode.nextnode

    def get_head(self):
        return self.head


if __name__ == "__main__":
    linkedlist = LinkedList()
    linkedlist.insertEnd(122)
