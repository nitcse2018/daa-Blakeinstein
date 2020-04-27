import sys
class Graph: 
    def __init__(self, vertices): 
        self.vertices
        self.edges = []
        
    def addEdge(self,u,v,w): 
        self.edges.append([u,v,w])
        
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 
    
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
            
    def KruskalMST(self): 
  
        result =[]
        i = 0
        e = 0
        self.edges =  sorted(self.edges,key=lambda item: item[2]) 
  
        parent = [] ; rank = []
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0)
        while e < self.V -1 :
            u,v,w =  self.edges[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 
            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)
        print ("Following are the edges in the constructed MST")
        for u,v,weight  in result:  
            print ("%d -- %d == %d" % (u,v,weight))
    
    def printMST(self, parent): 
        print ("Edge \tWeight")
        for i in range(1, self.V): 
            print parent[i], "-", i, "\t", self.graph[i][ parent[i] ]
    def minKey(self, key, mstSet):
        min = sys.maxint 
  
        for v in range(self.V): 
            if key[v] < min and mstSet[v] == False: 
                min = key[v] 
                min_index = v 
  
        return min_index
    def primMST(self):
        key = [sys.maxint] * self.V 
        parent = [None] * self.V
        key[0] = 0 
        mstSet = [False] * self.V 
  
        parent[0] = -1
  
        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
                        key[v] = self.graph[u][v] 
                        parent[v] = u 
  
        self.printMST(parent) 
  