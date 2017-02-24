from __future__ import print_function
class Vertex:
    def __init__(self,name):
        self.name=name

class Graph:
    vertices={}
    edges=[]
    edge_indices={}
    def addVertex(self,v):
        if isinstance(v,Vertex) and v not in self.vertices:
            self.vertices[v.name]=v

            for row in self.edges:
                row.append(0)
            self.edges.append([0]*(len(self.edges)+1))
            self.edge_indices[v.name]=len(self.edge_indices)
            print(self.edge_indices)
            return True
        else:
            return False
    def addEdge(self,u,v,weight=1):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]]=weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
    def printGraph(self):
        for i in self.edges:
            for j in i:
                print(j,end="")
            print()

g= Graph()
for i in range(ord('A'),ord('F')+1):
    g.addVertex(Vertex(chr(i)))

edges=['AB','AC','AD','EF','CF','CD']

for i in edges:
    g.addEdge(i[:1],i[1:])

g.printGraph()
