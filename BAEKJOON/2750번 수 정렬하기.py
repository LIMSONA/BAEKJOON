# 첫째 줄 개수 n
# 둘째줄부터 n개의 줄 수 주어짐
# 출력 오름차순으로 하나씩 출력

import sys

n=int(sys.stdin.readline())
numlist=[]
for _ in range(n):
    num=int(sys.stdin.readline())
    numlist.append(num)
numlist.sort()

for i in numlist:
    sys.stdout.write(str(i)+'\n')