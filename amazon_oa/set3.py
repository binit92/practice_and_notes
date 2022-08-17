# Given an array of points where points[i] = [xi, yi] represents a point in X-Y plane
# and an integer k closet points to the origin(0,0)
# Euclidean distance - square root of (x1-x2)^2 + (y1-y2)^2

# Return the kcloset points 
# leetcode problem : 973: K Closet Points to Origin 

def kClosest(points , k):
    points.sort(key = squared_distance)
    return points[:k]

def squared_distance(point):
    return point[0] ** 2 + point[1] ** 2


# if __name__ == '__main__':
#     points = [[3,3],[5,-1],[-2,4]]
#     k = 2
#     print(kClosest(points,k))

# rainfall 
# Amazon Alexa AI team is working to add feature that suggest days for camping based on the weather forecast.
# According to survey, a day is ideal for camping if the amount of the rainfall has been non-increasing 
# for prior k days from the considered day and will be non-decreasing for the following k days from the 
# considered day. Given the predicted rainfall for the next n days, find all all ideal days 
# day = [3,2,2,2,3,4]
# k = 2 
# answer is [3,4]

def rainfall(arr, k):
    output = []
    for i in range(k, len(arr) - k):
        l = arr[:i + k + 1]
        r = arr[i + k: ]
        if min(l) >= arr[i] <= min(r):
            output.append(i + 1)
    return output

# https://leetcode.com/discuss/interview-question/1482144
# Testcase1
# INSERT fries 4
# INSERT soda 2
# VIEW - - 
# VIEW - -
# INSERT hamburger 5
# VIEW - - 
# INSERT nuggets 4
# INSERT cookie 1
# VIEW - -
# VIEW - -

# Output - 
# soda
# fries
# hamburger
# nuggets
# hamburger

import heapq

class CustomHeap:
    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)
        self.viewCount = 0

    def addToHeap(self, priority, name):
        heapq.heappush(self.heap,(priority, name))

    def view(self):
        self.viewCount += 1
        return heapq.nsmallest(self.viewCount,self.heap)[-1]

if __name__ == '__main__':
    cHeap = CustomHeap()
    cHeap.addToHeap(4,'fries')
    cHeap.addToHeap(2,'soda')
    print(cHeap.view()[1])
    print(cHeap.view()[1])
    cHeap.addToHeap(5,'hamburger')
    print(cHeap.view()[1])
    cHeap.addToHeap(4,'nuggests')
    cHeap.addToHeap(1,'cookie')
    print(cHeap.view()[1])
    print(cHeap.view()[1])
    
