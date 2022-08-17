import math
def sumofmax(num):
    

    maximum = float("-inf")
    second_maximum = float("-inf")
    for val in num:
        
        val = math.floor(val);
        
        if val > maximum :
            second_maximum = maximum
            maximum = val
        elif val < maximum and val > second_maximum:
            second_maximum = val

    return maximum + second_maximum

if __name__ == '__main__':

    num =  [100, 5, 3, 1000, 20]
    print(sumofmax(num))
    assert  1100, sumofmax(num)

    # maximum is duplicate 
    num = [-100, 0 , 100, 100, 33, 22]
    print(sumofmax(num))

    #
    num = [1,1,2]
    print(sumofmax(num))

    # 
    num = [1.0, 2.5, 3.2, 4]
    print(sumofmax(num))

