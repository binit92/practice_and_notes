class UnionFind:
    def __init__(self, size):
        self.arr = [0] * size
        self.rank = [0] * size
        for i in range(size):
            self.arr[i] = i
            self.rank[i] = 1

    def find(self,x):
        while x != self.arr[x]:
            x = self.arr[x]
        return x

    def union(self, x, y):
        xVal = self.find(x)
        yVal = self.find(y)
        if xVal != yVal :
            if self.rank[x] < self.rank[y]:
                self.arr[yVal] = xVal
            elif self.rank[y] > self.rank[x]:
                self.arr[xVal] = yVal
            else:
                self.arr[xVal] = self.arr[yVal]
                self.rank[xVal] += 1
            

    def connected(self, x, y):
        return self.find(x) == self.find(y)


# Test Case
uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true