# Ordered Linked List
class ListNode:
    def __init__(self) -> None:
        self.data = None
        self.pointer = -1

class LinkedList:
    def __init__(self,size) -> None:
        self.startPtr = 0
        self.freePtr = 0
        self.nullPtr = -1
        self.container = [ListNode() for x in range(size)]
        self.size = size
    
    def initialiseList(self):
        self.startPtr = self.nullPtr
        self.freePtr = 0

        for x in range(self.size - 1):
            self.container[x].pointer = x + 1
        self.container[self.size - 1].pointer = self.nullPtr

    def insertNode(self, newItem):
        if self.freePtr != self.nullPtr:
            newNodePtr = self.freePtr
            self.container[newNodePtr].data = newItem
            self.freePtr = self.container[self.freePtr].pointer

            thisNodePtr = self.startPtr
            prevNodePtr = self.nullPtr

            while thisNodePtr != self.nullPtr and self.container[thisNodePtr].data < newItem:
                prevNodePtr = thisNodePtr
                thisNodePtr = self.container[thisNodePtr].pointer
            
            if prevNodePtr == thisNodePtr:
                self.container[newNodePtr].pointer = self.startPtr
                self.startPtr = newNodePtr
            else:
                self.container[newNodePtr].pointer = thisNodePtr
                if prevNodePtr != self.nullPtr:
                    self.container[prevNodePtr].pointer = newNodePtr
                else:
                    self.startPtr = newNodePtr
                
            
    def displayStatus(self):
        i = self.startPtr
        print("Start Pointer: ", self.startPtr)
        print("Free Pointer: ", self.freePtr)
        while i != self.nullPtr:
            print(f"Index: {i} | Data: {l1.container[i].data}  | Pointer: {l1.container[i].pointer}")
            i = self.container[i].pointer



# driver code
n = 10
l1 = LinkedList(n)
l1.initialiseList()

l1.insertNode("E")
l1.insertNode("G")
l1.insertNode("B")
l1.insertNode("A")
l1.insertNode("F")
l1.insertNode("C")

l1.displayStatus()