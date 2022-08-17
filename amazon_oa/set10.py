# leetcode.com/discuss/interview-question/1829038/amazon-oa-numberofbricks
# TODO: Can it be solved in logarithmic time ?
# TODO: Can it be solved in constant time  ?

def findlastOne(num):

    i = 1
    current = 0

    lastBrickCount =0
    lastAddedBy = 0

    while i <= num:
        
        if current + i >= num:
            lastBrickCount = num - current
            lastAddedBy = 1
            break
        else:
            current += i
            #print(current, end = "")

        if current + (i * 2) >= num:
            lastBrickCount = num - current
            lastAddedBy = 2
            break
        else:
            current += i * 2
            #print(current, end = "")

        i+=1

    return (lastAddedBy,lastBrickCount) 

if __name__ == '__main__':
    print(findlastOne(13))
    print(findlastOne(10))
    print(findlastOne(11))
