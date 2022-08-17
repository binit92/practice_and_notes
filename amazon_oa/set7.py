# https://www.desiqna.in/5059/amazon-oa-coding-questions-and-solutions-set-7-2022

# Approach : start from end, whenever you could sum, (where a[i-1] < a[i]), do it

def packaging(packages):
    length = len(packages)
    i = length -1 
    while i >= 1:
        if packages[i-1] < packages[i]:
            packages[i-1] += packages[i]
            del packages[i]  
        i -= 1      

    return packages

if __name__ == '__main__':
    test1 = [2,9,10,3,7]
    print(packaging(test1))