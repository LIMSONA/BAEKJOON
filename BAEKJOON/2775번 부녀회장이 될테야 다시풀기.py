import sys

t=int(sys.stdin.readline())

for _ in range(t):
    k=int(sys.stdin.readline())
    n=int(sys.stdin.readline())

    apt=[[0,1] for i in range(k+1)]

    for a in range(2,n+1):
        apt[0].append(a)
    
    for floor in range(1,k+1):
        for room in range(2,n+1):
            x=apt[floor][room-1]+apt[floor-1][room]
            apt[floor].append(x)
                   
    print(apt[k][n])