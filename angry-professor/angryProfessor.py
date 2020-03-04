import math
import os
import random
import re
import sys


def angryProfessor(k, a):
    leng=len(a)
    check=0
    for i in range(leng):
        if a[i]<=0:
            check=check+1
    if check>=k:
        out="NO"
    else:
        out="YES"
    return out

if __name__ == '__main__':
    a=[-1,-2,-3,5,6,7]
    k=2
    print(angryProfessor(k,a))
