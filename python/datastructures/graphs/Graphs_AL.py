class Vertex:
    def __init__(self,n):
        self.name=n
        self.neighbors=[]
    def addNeighbors(self,x):
        if x not in self.neighbors:
            self.neighbors.append(x)
            self.neighbors.sort()


class Graph:
    vertices={}
    def addVertex(self,vertex):
        if isinstance(vertex,Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name]=vertex
            return True
        else:
            return False
    def addEdge(self,u,v):
        if u in self.vertices and v in self.vertices:
            for key,value in self.vertices.items():
                if key==u:
                    value.addNeighbors(v)
                elif key==v:
                    value.addNeighbors(u)
            return True
        else:
            return False
    def printGraph(self):
        for key in sorted(self.vertices.keys()):
            print(key + str(self.vertices[key].neighbors))



g= Graph()
for i in range(ord('A'),ord('F')+1):
    g.addVertex(Vertex(chr(i)))

edges=['AB','AC','AD','EF','CF','CD']

for i in edges:
    g.addEdge(i[:1],i[1:])

g.printGraph()
