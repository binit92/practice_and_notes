class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # Create Adjacency List 
        adjList = {}
        for val in times:
            if not val[0] in adjList:
                adjList[val[0]] = [val[1:]]
            else:
                adjList[val[0]].append(val[1:])
            
        print(adjList)
        
        # Sort the edges 
        for key,val in adjList.items():
            print(val)
            val.sort(key = lambda x : x[1])
        
        print(adjList)
        
        signal = [float("inf")] * (n+1)
        
        
        def DFS(signal, currNode, currTime):
            if(currTime >= signal[currNode]):
                return
            
            
            signal[currNode] = currTime
            
            if not currNode in adjList:
                return
            
            for val in adjList[currNode]:
                print(val)
                nextEdge = val[0]
                weight = val[1]
                DFS(signal, nextEdge, currTime + weight)
            
        
        
        print("before: ", signal)
        DFS(signal, k, 0);
        print("after: ", signal)
        
        answer = -float("inf")
        for i in range(1, n):
            answer = max(answer,signal[i])
        
        if answer == float("inf"):
            return -1
        return answer