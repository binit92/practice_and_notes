# leetcode 1010 : Pairs of Songs with Total Durations Divisible by 60 

from collections import defaultdict


def num_of_pairs(arr):
    remainders = defaultdict(int)
    ret = 0 
    for val in arr:
        if val %60 == 0 :
            ret = ret + remainders[0]
        else :
            ret = ret + remainders[60 - val%60]
        remainders[val%60] += 1
    return ret

