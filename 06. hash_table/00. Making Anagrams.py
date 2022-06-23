#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
"""
cde -> {
    c : 1
    d : 1
    e : 1
}
abc -> {
    a : 1
    b : 1
    c : 1
}

s1 -> c

"""

def makeAnagram(a, b):
    s1 = Counter(a)
    s2 = Counter(b)

    count = 0

    for i in s1:
        if i in s2:
            count += min(s1[i], s2[i]) * 2
    return (len(a) + len(b)) - count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
