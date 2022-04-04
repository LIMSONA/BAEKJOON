t= int(input()) #몇 문제

score= list(map(int, input().split())) # 채점

result=0
seq=1

for i in range(t):
    if score[i]==1: 
        result+=seq #총점
        seq+=1 # 연속
    else:
        seq=1 #다시 리셋
    
print(result)