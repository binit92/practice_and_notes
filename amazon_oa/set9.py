# Find the password strength 
# leetcode.com/discuss/interview-question/1471459/Amazon-OA

def passwordStrength(password):
    vowels = ['a','e','i','o','u']
    ret = []
    vowelFound = False
    consonantsFound = False
    lastIndex = 0
    for i in range(len(password)):
        if password[i] in vowels:
            vowelFound = True
        else:
            consonantsFound = True

        if vowelFound and consonantsFound:
            ret.append(password[lastIndex:i+1])
            vowelFound = False
            consonantsFound = False
            lastIndex = i + 1
    print(ret)
    return len(ret)


# problem 2 
# Sort 1's and 0's in array to the end. Either end is fine.
# Find the minimum number of adjacent swaps required to sort.

def minimumAdjacentSwap(items):
    
    def moveToLeft(items, target):
        count = 0
        lastVal = 0 
        for i in range(len(items)):
            if items[i] == target:
                count += i - lastVal
                lastVal += 1
        return count 
    return min(moveToLeft(items,0) , moveToLeft(items,1))


if __name__ == '__main__':
    test1 = "thisisbeautiful"
    test2 = "hackerrank"
    test3 = "aeiou"

    print(passwordStrength(test1))
    print(passwordStrength(test2))
    print(passwordStrength(test3))

    test4  = [1,1,1,0,0,0]  # 0
    test5 = [0,0,0,1,1,1]  # 0
    test6 = [0,0,0,0,1,0,1,0,0] # 5
    test7 = [0,0,1,0,1,0] # 3
    print(minimumAdjacentSwap(test4))
    print(minimumAdjacentSwap(test5))
    print(minimumAdjacentSwap(test6))
    print(minimumAdjacentSwap(test7))