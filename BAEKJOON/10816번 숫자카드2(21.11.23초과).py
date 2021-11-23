import sys

n=int(sys.stdin.readline())#상근이 숫자카드개수
ncard=list(map(int,sys.stdin.readline().split()))
ncard.sort()

m=int(sys.stdin.readline())
mcard=list(map(int,sys.stdin.readline().split()))




# #count로 찾아보기(시간초과)--------------------------------
# for i in mcard:
#     print(ncard.count(i),end=" ")
    