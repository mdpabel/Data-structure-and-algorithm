#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

"""
cdcd
c d c d
cd dc cd
cdc dcd

{
    c : 2
    d : 2
    cd : 3
    ccd : 1
    cdd : 1
}
n-1 * n /2
3 * 4



"""

def sherlockAndAnagrams(s):
    # Write your code here
    n = len(s)
    map = defaultdict(int)

    for i in range(n):
        for j in range(n-i):
            sorted_item = "".join(sorted(s[j:j+i+1]))
            map[sorted_item] += 1

    count = 0
    for item in map:
        if map[item] > 1:
            n = map[item]
            count += ((n - 1) * n) // 2
    return count





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
