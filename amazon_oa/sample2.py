
from logging.config import valid_ident


class Node():
    def __init__(self, val, left,right):
        self.val = val
        self.left = left
        self.right = right


def findHeight(num):
    # base case 
    if num is None :
        return 0
    elif num.left is None and num.right is None:
        return 1

    return 1 + max(findHeight(num.left), findHeight(num.right)) 

def findWidth(num):

    # 1
    # 2 3
    # 4 5 6 7 

    # 1 , 2 , 3 , 2 , ....

    queue = [num]
    maximum = float("-inf")
    while queue:
        size = len(queue)
        temp = []
        for i in range(0,size):            
            node = queue.pop(0)
            # append the child into the queue 
            if not node.left is None:
                temp.append(node.left)
            
            if not node.right is None:
                temp.append(node.right)
        
        maximum = max(maximum,len(temp))
        queue = temp

    return maximum # 2


if __name__ == '__main__':
    n4 = Node(4, None, None)
    n2 = Node(2, n4, None)
    n3 = Node(3, None, None)
    n1 = Node(1, n2, n3)

    print(findHeight(n1),3)    
    
    
    