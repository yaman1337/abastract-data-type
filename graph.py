class graph:
    def __init__(self) -> None:
        self.container = {}
        self.no_of_vertex = 0

    def addVertex(self, v):
        if v not in self.container:
            self.container[v] = []
            self.no_of_vertex += 1
        else:
            print(f"Vertex {v} already exists in graph.")
    
    def addEdge(self, v1, v2, weight):
        if v1 in  self.container:
            for arr in self.container[v1]:
                if(arr[0] == v2):
                    print(f"Edge {v2} already exists.")
                    break

            self.container[v1].append([v2, weight])
            print(f"Add edge {v1} to {v2} with weight of {weight}.")
                
    def findPath(self, start, end, path=[]):
        graph = self.container

        path = path + [start]
        if start == end:
            return path
        
        if start not in graph:
            return None
        
        for node in graph[start]:
            if node[0] not in path:
                newPath = self.findPath(node[0], end, path)
                if newPath: 
                    return newPath
        return None
        
        
    def displayInfo(self):
        print("""============== Display graph  ===============""")
        print(self.container)

g1 = graph()

# add vertices

g1.addVertex("A")
g1.addVertex("B")
g1.addVertex("C")
g1.addVertex("D")
g1.addVertex("E")

# add edges
g1.addEdge("A", "B", 3)
g1.addEdge("A", "C", 4)
g1.addEdge("A", "D", 2)
g1.addEdge("B", "E", 4)

print("============== Path ==============")
print(g1.findPath("A", "E"))

g1.displayInfo()