class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        
        adjlist = [ [] for i in range(n)]
        for a, b in edges:
            adjlist[a].append(b)
            adjlist[b].append(a) # both sides

        print(adjlist)

        stack = [start] # stack
        seen = set()    # set 

        while start:
            top = stack.pop() # popping top items 
            
            if top == end:    # when destination is reached 
                return True

            if top in seen:  # if already seen 
                continue

            for val in adjlist[top]: # add the neighbours 
                stack.append(val)

        return False

    
# time complexity O(V+E)


if __name__ == '__main__':
    for x in range(2,4):
        y =2 
        while y <4:
            print(x**y)
            y+=1