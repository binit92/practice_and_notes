# https://leetcode.com/problems/robot-bounded-in-circle/

def isRobotBounded(instructions):

    #north = 0, east = 1, west = 2, south = 3
    x,y = 0,0
    idx = 0
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    for val in instructions:
        if val == "L":
            idx = (idx + 3 ) % 4
        elif val == "R":
            idx = (idx + 1) % 4
        else:
            x += directions[idx][0]
            y += directions[idx][1]
    return (x == 0 and y == 0) or idx != 0 

if __name__ == '__main__':
    test1 = "GGLLGG"
    print(isRobotBounded(test1))
    
    test2 = "GG"
    print(isRobotBounded(test2))
    
    test3 = "GL"
    print(isRobotBounded(test3))