import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    if max(a)==min(b):
        return 1
    elif max(a)>min(b):
        return 0
    else:
        out=0;
        for i in range(max(a),min(b)+1):
            status=1
            for j in range(len(a)):
                if i%a[j]!=0:
                    status=0
            for j in range(len(b)):
                if b[j]%i!=0:
                    status=0
            if status==1:
                out=out+1
        return out



if __name__ == '__main__':
    arr=[2,4]
    brr=[16,32,96]

    total = getTotalX(arr, brr)

    print(total)
