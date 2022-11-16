class Node:
    def __init__(self) -> None:
        self.data = ""
        self.leftPtr = 0
        self.rightPtr = 0

class Tree:
    def __init__(self, size) -> None:
        self.container = [Node() for i in range(size)]
        self.size = size
        self.nullPtr = -1
        self.freePtr = 0
        self.rootPtr = self.nullPtr
    
    def initialiseTree(self):
        self.freePtr = 0
        self.rootPtr = self.nullPtr
        for i in range(self.size - 1):
            self.container[i].leftPtr = i + 1
        self.container[self.size - 1].leftPtr = self.nullPtr

    def insertNode(self, newItem):
        if self.freePtr != self.nullPtr:
            newNodePtr = self.freePtr
            self.freePtr = self.container[newNodePtr].leftPtr
            self.container[newNodePtr].data = newItem
            self.container[newNodePtr].leftPtr = self.nullPtr
            self.container[newNodePtr].rightPtr = self.nullPtr

            if self.rootPtr == self.nullPtr:
                self.rootPtr = newNodePtr
            else:
                thisNodePtr = self.rootPtr
                prevNodePtr = self.nullPtr
                turnedLeft = False
                while thisNodePtr != self.nullPtr:
                    prevNodePtr = thisNodePtr
                    if self.container[thisNodePtr].data > newItem:
                        turnedLeft = True
                        thisNodePtr = self.container[thisNodePtr].leftPtr
                    else:
                        turnedLeft = False
                        thisNodePtr = self.container[thisNodePtr].rightPtr
                if turnedLeft == True:
                    self.container[prevNodePtr].leftPtr = newNodePtr
                else:
                    self.container[prevNodePtr].rightPtr = newNodePtr
    def findElement(self, itemToFind):
        node = -1
        for i in range(self.size):
            if self.container[i].data == itemToFind:
                node = i
                break
        return node
        
    
    def displayContainer(self):
        print(f"FreePtr: {self.freePtr} | RootPrt: {self.rootPtr}")
        print("------------------------------------")
        for i in range(self.size):
            print(f"Node: {i} | Left Pointer: {self.container[i].leftPtr} | Data: {self.container[i].data} | Right Pointer: {self.container[i].rightPtr}")
        print("-----------------------------------")


t1 = Tree(size=5)
t1.initialiseTree()

t1.insertNode("B")
t1.insertNode("C")
t1.insertNode("A")
t1.insertNode("E")
t1.insertNode("D")


t1.displayContainer()


print("Searching for A ..")
res = t1.findElement("A")
if res == -1:
    print("Item not found")
else:
    print(f"Item in node {res}")