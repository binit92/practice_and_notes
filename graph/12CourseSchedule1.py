class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = { i : [] for i in range(numCourses)}
        for u,v in prerequisites:
            adjList[u].append(v)
            
        
        visited = set()
        
        def dfs(node):
            
            # for cycles 
            if node in visited:
                return False
            
                    
            if adjList[node] == []:
                return True
            
            visited.add(node)
            
            
            for val in adjList[node]:
                if not dfs(val):
                    return False
            
            # remove the course that we can visit .. 
            visited.remove(node)
            adjList[node] = []
            return True
        
        # run for all the unconnected files .. 
        for val in range(numCourses):
            if not dfs(val):
                return False
            
        return True