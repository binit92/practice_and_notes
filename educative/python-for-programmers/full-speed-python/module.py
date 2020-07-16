import math
def myCourse(name):
    print("Course:" + name)
    
def findGCD(a,b):
    return math.gcd(a,b)

def calculateSinCosTan(x):
    sin = math.sin(x)
    cos = math.cos(x)
    tan = math.tan(x)
    return [sin, cos, tan]

def findMaximum(x,y):
    return max(x,y)

def isDivisible(x,y):
    return x%y == 0

def fibonacci(x):
    
    if x<=0:
        return 1
    elif x == 1:
        return 1
    else:
        val = fibonacci(x-1) + fibonacci(x-2)
        return val
    
def sum_N_Numbers (n):
    if n<1:
        return 0
    else: 
        return sum_N_Numbers(n-1) + n