# https://www.geeksforgeeks.org/connect-n-ropes-minimum-cost/

# The cost to connect two ropes is the sum of their lengths 
# 4 3 2 6 
# 2 3 4 6 (SORT)
# 5 4 6   (5)
# 4 5 6 (SORT)
# 9 6  (9)
# 6 9 (SORT)
# 15   (15)
# total cost = 5 + 9 + 15 = 29

import heapq

def minCost(arr):
    # Create a priority queue out of the given list
    heapq.heapify(arr)

    # Initialize result
    res = 0

    # While size of priority queue is more than 1 
    while (len(arr) > 1):
        # Extract shortest two ropes from arr
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)

        # connect the ropes: update 
        res += first + second
        heapq.heappush(arr, first + second)
    return res

if __name__ == '__main__':
    lengths = [4, 3, 2, 6]    
    print("total cost ", minCost(lengths))