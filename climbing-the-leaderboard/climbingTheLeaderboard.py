import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    scores=list(dict.fromkeys(scores))
    ind=len(scores)-1
    k=len(alice)
    tres=scores[0]
    out=[]
    for i in range(k):
        status=1
        while status==1:
            if alice[i]>=tres:
                out.append(1)
                status=0
            else:
                if alice[i]<scores[ind]:
                    status=0
                    out.append(ind+2)

                else:
                    ind=ind-1
    return out





if __name__ == '__main__':
    scores=[100,100,50,40,40,20,10]
    alice=[5,25,50,120]

    result = climbingLeaderboard(scores, alice)

    print(result)
