import numpy as np

n,m = map(int,input().split())

# n개줄에 원소m개가 주어짐
a,b= [],[]
for i in range(n):
    a.append( list(map(int,input().split())) )
for i in range(n):
    b.append( list(map(int,input().split())) )


A= np.array(a)
B= np.array(b)
result= A+B 

#array 형태를 리스트로 바꿔주기
result_2= result.tolist()

for i in result_2:
    print(" ".join(map(str,i)))