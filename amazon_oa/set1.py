# The interns At Amazon were asked to review the company's tock value over a period
# Give the stock price of n months, the net price change for the ith
# month is defined as absolute difference between the average of stock prices 
# for the first i months and of the remaining (n-i) months
# where, i<= i < n
# Note: these averages are rounded down to an integer

# Given an array of stock prices, find the month at which the net price
# change is minimum , if there are several such months, return the earliest month 

# stockPrice = [1,3,2,3]
# 1st month (1) - (3+2+3) = 1 - 2=  1 
# 2nd month (1,3) - (2,3) =  2- 2 = 0  [ANS:2 ]
# 3rd month (1,3,2) - (3) = 3 -3 = 0
# 4th month (1,3,2,3) - (0) = 4 

# stockPrice = [1,1,1,1,1,1]
# 1st month  = (1) - (1+1+1+1+1) = 0 [ANS: 1]

# stockPrice = [1,3,2,4,5]
# 1st month = (1) - (3+2+4+5) = 1 - 14/4 = 1-3 = 2
# 2nd month = (1+3) - (2+4+5) = 2 - 3 = 1  [ANS: 2] 
# 3rd month = (1+3+2) - (4+5) = 2 - 4 = 2
# 4th month = (1+3+2+4) - (5) = 2 -5 = 3 
 

def findEarliestMonth(stockPrice) :
    n = len(stockPrice)
    minimum = float('inf')
    ret = -1
    for i in range(1, n-1):
        left = sum(stockPrice[0:i]) // (i)
        right = sum(stockPrice[i : n]) // (n- i)
        #print(stockPrice[0:i], " -> " , stockPrice[i:n])
        #print(left , " ", right)

        diff = abs(left-right)
        #print("diff:" , diff)
        if diff == 0:
            return i
        
        if diff < minimum:
            minimum = diff
            ret = i
    return ret

if __name__ == '__main__':
    test1 = [1,3,2,3]
    result1 = 2
    print(findEarliestMonth(test1))
    #assert(findEarliestMonth(test1) == result1)

    test2 = [1,1,1,1,1]
    result2 = 1
    print(findEarliestMonth(test2))
    #assert(findEarliestMonth(test2) == result2)

    test3 = [1,3,2,4,5]
    result3 = 2
    print(findEarliestMonth(test3))
    #assert(findEarliestMonth(test3) == result3)