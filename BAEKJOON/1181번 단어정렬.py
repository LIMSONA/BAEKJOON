# 길이가 짧은 것
# 길이 같은면 사전 순(sort)

# 1차시도---------------------

import sys
n=int(sys.stdin.readline())

# 2차원 리스트를 만들어요
# ex)단어길이가 1이면 list[1]에 들어감
len_list=[[]*51 for _ in range(51)] 

for _ in range(n):
    num=input()
    len_list[len(num)].append(num)
    
# sort 진행하고 출력해요
for i in range(1,51):
    len_list[i].sort()
    for j in len_list[i]:
        print(j)
        
#2차시도--------------------------------------        
import sys
n=int(sys.stdin.readline())

# 2차원 리스트를 만들어요
# ex)단어길이가 1이면 list[1]에 들어감
len_list=[[] for _ in range(51)] 

for _ in range(n):
    num=input( )
    len_list[len(num)].append(num)
    
# sort 진행하고 출력해요
for i in range(1,51):
    #len_list[i]리스트 값을 set로 바꿔서 중복제거
    len_list[i]=set(len_list[i])
    #다시 list로 바꿔서 sort하기
    len_list[i]=list(len_list[i])
    len_list[i].sort( )
    
    for j in len_list[i]:
        print(j)