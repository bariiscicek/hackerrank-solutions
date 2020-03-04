import random
def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index

            index += 1

    return -1


def nextMove(n,r,c,grid):
    for i in range(n):
        check=find_str(grid[i],"m")
        if check >=0:
            index1=i
            index2=check
    for i in range(n):
        check=find_str(grid[i],"p")
        if check >=0:
            indexx1=i
            indexx2=check
    dif1=index1-indexx1
    dif2=index2-indexx2
    if dif1 != 0:
        if dif1<0:
            return "DOWN"
        elif dif1>0:
            return "UP"
    elif dif2 != 0:
        if dif2<0:
            return "RIGHT"
        elif dif2>0:
            return "LEFT"


n=5
r=2
c=3
px=random.randint(0,4)
py=random.randint(0,4)
grid=[]
for i in range(n):
    inp=''
    for j in range(n):
        if i==r and j==c:
            inp=inp+'m'
        elif i==px and j==py:
            inp=inp+'p'
        else:
            inp=inp+'-'
    grid.append(inp)
print(grid)




print(nextMove(n,r,c,grid))
