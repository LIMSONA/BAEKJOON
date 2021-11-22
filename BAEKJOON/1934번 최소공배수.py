t=int(input())

for _ in range(t):
    a,b=map(int,input().split())
    import math
    print(math.lcm(a,b))