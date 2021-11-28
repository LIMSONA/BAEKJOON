#순열 라이브러리 알고있으면 겁나 쉬운 문제!
# m개 중 n개 뽑기! 순서상관있음!

import itertools

m,n=map(int,input().split())
result=itertools.permutations(range(1,m+1),n)

for i in result:
    print(*i) #안에 든거가 하나씩 나와야하니까