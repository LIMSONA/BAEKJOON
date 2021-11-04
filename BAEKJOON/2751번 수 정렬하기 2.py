# n개의 수 주어졌을때. 오름차순으로 정렬하는
# 둘째줄부터 n개의 줄에는 수가 주어지고 수는 중복x

import sys
n=int(sys.stdin.readline())
num=[]
for _ in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()

for i in num:
    print(i)

