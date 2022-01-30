# N개중 K개 뽑기
# n!/(n-k)!k!

from itertools import combinations
n,k= map(int,input().split())
result = len(list(combinations(range(1,n+1),k)))
print(result)

