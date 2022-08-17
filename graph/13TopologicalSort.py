class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i : [] for i in range(numCourses)}
        
        for u,v in prerequisites:
            adjList[u].append(v)
            
        visited = set()
        cycle = set()
        output = []
        
        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True
           
            
            cycle.add(node)
            for neigh in adjList[node]:
                if not dfs(neigh):
                    return False
                
            cycle.remove(node)
            visited.add(node)
            output.append(node)
            return True
        
        for val in range(numCourses):
            if not dfs(val):
                return []
        
        return output
                
        