#User function Template for python3


class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        
        colors = [0] * V
        
        def hasCycle(node):
            
            if colors[node] == 1:
                return True
            if colors[node] == 2:
                return False
            
            colors[node] = 1
            
            for neigh in adj[node]:
                
                if hasCycle(neigh):
                    return True
            
            colors[node] = 2
            return False
            
        
        for node in range(V):
            if colors[node] == 0:
                if hasCycle(node):
                    return True
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends