# 그룹단어는 연속된 문자 뒤에 또 나오면 안된다
# 그룹단어 갯수 출력

import sys

n=int(sys.stdin.readline())

cnt=0
for _ in range(n):
    t=list(input()) #sys로 받으면 '\n'까지 리스트에 들어감
    t_check=[ ] #거쳐간 문자열 리스트
    
    for i in range(1,len(t)):
        #<< 조건1. 연속 vs 비연속 >>
        if t[i]==t[i-1]:    #연속
            continue
    
        else:    #비연속
            t_check.append(t[i-1]) #거쳐간 문자열 리스트에 넣기
            
            #<<조건2. new 단어 vs old 단어>>
            if t[i] not in t_check: #이전에 안나온 new단어
                continue    
           
            else:   #이전에 나온 old단어 
                cnt+=1
                break #중단

print(n-cnt) #총 개수에서 old단어개수 빼기