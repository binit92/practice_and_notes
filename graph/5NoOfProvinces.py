# Union Find Class 
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size

    # path compression 
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x]) #recursive
        return self.root[x]

    # the union function by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1

    def getCount(self):
        return self.count

class Solution:
    def findCircleNum(self, isConnected):
        if not isConnected or len(isConnected) == 0:
            return 0
        n = len(isConnected)
        uf = UnionFind(n)
        for row in range(n):
            for col in range(row+1,n):
                if isConnected[row][col] == 1:
                    uf.union(row, col)
        return uf.getCount

