class UnionFind:
    def __init__(self,size):
        self.parent ={i:i for i in range(size)}
        self.rank = {i: 0 for i in range(size)}
        self.number_province = size
        
        
        # self.rank = [1] * size
    def find(self,v):
        
        #path compression
        if self.parent[v] == v:
            return v
        self.parent[v] = self.find(self.parent[v])
        
        return self.parent[v]
    
    def union(self,x,y):
        xp,yp = self.find(x),self.find(y)
        
        #merge by rank
        if xp != yp:
            self.number_province -= 1
            if self.rank[xp]  < self.rank[yp]:
                xp, yp = yp, xp
                
            self.parent[yp] = xp
            self.rank[xp] +=1 
    
    def answer(self):
        return self.number_province
    
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i != j and isConnected[i][j] == 1:
                    uf.union(i,j)
        
        return uf.answer()
