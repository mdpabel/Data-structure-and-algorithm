#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    stack = []
    map = {
        ")" : "(",
        "}" : "{",
        "]" : "["
    }

    if len(s) % 2 == 1:
        return "NO"

    for item in s:
        if item == "(" or item == "{" or item == "[":
            stack.append(item)
        elif len(stack) == 0:
            return "NO"
        elif len(stack) and (stack.pop() != map[item]):
            return "NO"


    if len(stack) > 0:
        return "NO"
    else:
        return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
