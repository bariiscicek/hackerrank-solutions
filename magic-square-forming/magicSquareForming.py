
import math
import os
import random
import re
import sys

def formingMagicSquare(s):
    q = [0,0,0,0,0,0,0,0,0]
    ind=0
    for i in range(3):
        for j in range(3):
            q[ind]=s[i][j]
            ind=ind+1

    sol=[]
    sol.append([2,7,6,9,5,1,4,3,8])
    sol.append([2,9,4,7,5,3,6,1,8])
    sol.append([4,3,8,9,5,1,2,7,6])
    sol.append([4,9,2,3,5,7,8,1,6])
    sol.append([6,1,8,7,5,3,2,9,4])
    sol.append([6,7,2,1,5,9,8,3,4])
    sol.append([8,1,6,3,5,7,4,9,2])
    sol.append([8,3,4,1,5,9,6,7,2])
    minval=100000

    for i in sol:
        dst=0
        for j in range(9):
            dst=dst+abs(q[j]-i[j])
        if dst<minval:
            minval=dst
    return minval







s=[
[1,2,3],
[4,5,6],
[7,8,9]]

result = formingMagicSquare(s)
print(result)
