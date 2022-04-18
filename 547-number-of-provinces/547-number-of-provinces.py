class UnionFind:
    def __init__(self,size):
        self.parent ={i:i for i in range(size)}
        # self.rank = [1] * size
    def find(self,x):
        while(self.parent[x] != x):
            x = self.parent[x]         
        return x
            
    
    def union(self,x,y):
        xp,yp = self.find(x),self.find(y)
        # if self.rank[xp] < self.rank[yp]:
        #     xp,yp = yp,xp
            
        self.parent[yp] = xp
        # self.rankp[yp] += self.rank[xp]
        
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if i != j and isConnected[i][j] == 1:
                    uf.union(i,j)
        return len(set([uf.find(i) for i in range(len(isConnected))]))