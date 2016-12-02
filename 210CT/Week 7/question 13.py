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
            
    def addEdge(self, vertexFrom, vertexTo): # adds edges to the vertex
    
        if  vertexFrom in self.vertices: # checks if its in dic before doing anything
            for key, value in self.vertices.items():
                    if key == vertexFrom:
                        value.addNeighbor(vertexTo)

            if vertexTo in self.vertices: # checks if its in dic before doing anything
                for key, value in self.vertices.items():
                    if key == vertexTo:
                        value.addNeighbor(vertexFrom)
                        
    def adjacencyList(self): # stores the adjacency into graph
        for key in sorted(self.vertices.keys()): 
            self.graph[key] = set(self.vertices[key].neighbors)

    def Print(self): # prints the dictionary
        pprint(self.graph) #prints the formatted representation of the object
'''
Class vertex
vertex is represented by n stored in name
if the neighbours we are trying to add is not in the neighbours list then append it
then sort the list
class graph
empty vertices dictionary to store the vertices
empty grap dictionary to store the adjacency list
if the vertex we are trying to store is not in the vertices dictionary then adds it to the dictionary
before it starts adding edges it will make sure the vertices are in the dictionary
if they are the for loop wil go through the vertices and look for the 2 vertices and adds it to its neighbour
to store it to the graph dictionary
it goes through the vertices dictionary and stores the vertex with its neighbours to the graph dictionary
the key will be the vertex and the value will be the neighbours connected to that vertex
then the graph is printed 

'''

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
            neightbors = sorted neighbors
CLASS GRAPH

    vertices <- {}
    graph <- {}

    FUNCTION ADDVERTEX(VERTEX)
        IF vertex.name not in vertices thene
            vertices[vertex.name] <- vertex
            
    FUNCTION ADDEDGE(VERTEXFORM, VERTEXTO) 
        IF  vertexFrom in vertices then
            for key, value in vertices.items
                    IF key = vertexFrom then
                        value.addNeighbor(vertexTo)
            IF vertexTo in vertices then
                for key, value in vertices.items
                    IF key = vertexTo then
                        value.addNeighbor(vertexFrom)
  
    FUNCTION ADJACENCYLIST()
        for key in sorted vertices.keys
            graph[key] <- construct(vertices[key].neighbors)
    FUNCTION PRINT ()
        print(graph)

'''
