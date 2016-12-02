from pprint import pprint
class Vertex:
    
    def __init__(self, n):
        self.name = n
        self.neighbors = []

    def addNeighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neightbors = sorted(self.neighbors)
class Graph:
    def __init__(self):
        self.vertices = {}
        self.graph = {}

    def addVertex(self, vertex): #adds the vertex if the vertex is not there
        if vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
    def addEdge(self, vertexFrom, vertexTo): # adds edges to the vertex 
        if  vertexFrom in self.vertices:
            for key, value in self.vertices.items():
                    if key == vertexFrom:
                        value.addNeighbor(vertexTo)
            if vertexTo in self.vertices:
                for key, value in self.vertices.items():
                    if key == vertexTo:
                        value.addNeighbor(vertexFrom)
                return True
        else:
            return False

    def adjacencyList(self):
        for key in sorted(self.vertices.keys()): 
            self.graph[key] = set(self.vertices[key].neighbors)
    def Print(self):
        pprint(self.graph)

g = Graph()

a = Vertex('A')
b = Vertex('B')
c = Vertex('C')
d = Vertex('D')
e = Vertex('E')

g.addVertex(a)
g.addVertex(b)
g.addVertex(c)
g.addVertex(d)
g.addVertex(e)

g.addEdge('A','B')
g.addEdge('A','C')
g.addEdge('B','C')
g.addEdge('B','D')
g.addEdge('C','D')
g.addEdge('C','E')
g.addEdge('D','E')


g.adjacencyList()
g.Print()

            
'''
CLASS VERTEX
    
    name <- n
    neighbors <- []

    FUNCTION ADDNEIGHBOR(V)
        IF v not in neighbors then
            neighbors.append(v)
            neightbors <- sorted neigbors
CLASS GRAPH
    vertices <- {}

    FUNCTION ADDVERTEX(VERTEX)
        IF vertex not in vertices then
            vertices[vertex] = vertex
            return True
        else
            return False
    FUNCTION ADDEDGE(U, V)
        if u in vertices then
            if v in vertices then
                for key, value in vertices.items
                    if key = u then
                        value.addNeighbor(v)
                    if key = v then 
                        value.addNeighbor(u)
                return True
        else:
            return False

    FUNCTION ADJACENCYLIST
        for key in sorted list vertices.keys 
           print key self.vertices[key].neighbors
'''
