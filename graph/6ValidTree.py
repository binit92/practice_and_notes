class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        print(self.root)
        print(self.rank)

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False
        else:
            if self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            else: 
                self.root[rootX] = rootY
                self.rank[rootX] += 1
        return True

class Solution:
    def validTree(self, n, edges) -> bool:
        if len(edges) != n-1:
            return False
        else:
           
            uf = UnionFind(n)
            for row,val in edges:
                if not uf.union(row,val):
                    return False
        return True
                    
                    