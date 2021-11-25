#시간초과 (실패)---------------------------------------

#n과 2n사이의 소수
#False 카운트 방법

#소수 - 에라토스테네스의 체
import math

def prime(x):
    array=[True for i in range(x+1)]
    array[0]=False
    array[1]=False 
    if x==1: return 1
    for i in range(2,int(math.sqrt(x))+1):
        if array[i]==True:
            j=2
            while i*j<=x:
                array[i*j]=False
                j+=1
    return array.count(True) 

#기본 정보 입력받기
from sys import stdin
while True:
    n=int(stdin.readline())
    if n==0:
        break
    elif n==1:
        print(1)
        continue
    #정답 도출
    print(prime(2*n)-prime(n))