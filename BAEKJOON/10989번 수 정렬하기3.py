# n=int(input())
# num=[]
# for _ in range(n):
#     inp=int(input())
#     num.append(inp)
#     num.sort()
# for i in num:
#     print(i)

# import sys

# # for i in sys.stdin.readline():
# #     print(i)

# for i in sys.stdin:
#     print(i)

import sys

n = int(sys.stdin.readline())
lists = [0] * 11
for i in range(n):
    lists[int(sys.stdin.readline())] += 1	
    # 0으로 된 리스트의 인덱스를 입력 받고 해당 숫자가 존재하면 1을 더하는 방식. 
    #2이면 두 번 출력하도록 아래에서 진행
    
for i in range(10001):
    if lists[i] != 0:	# 우선 0이면 해당 숫자가 없는 것 이므로
        for j in range(lists[i]):	# 있으면 해당 숫자만큼
            print(i)	# 출력