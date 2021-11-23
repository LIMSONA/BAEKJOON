#시간초과(약수성질 소수판별 알고리즘이용)----------------------
def sosu(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:   
            return False
    return True

from sys import stdin
while True:
    n=int(stdin.readline())
    cnt=0
    if n==0:
        break
    elif n==1:
        print(1)
    else:
        for x in range(n,2*n+1):     
            if sosu(x):
                cnt+=1
        print(cnt)


#성공(에라토스테네스의 채 이용)---------------------------
def sosu(x):
    array=[True for _ in range(x+1)]
    for i in range(2,int(x**0.5)+1):
        if array[i]==True:
            j=2
            while i*j<=x:
                array[i*j] = False
                j+=1
    return [i for i in range(2,x) if array[i]==True]
    #array 인덱스를 가지고 소수리스트를 return하기 = result

while True:
    n= int(input())
    if n==0:break
    result=sosu(2*n+1) #1) 먼저 2n까지 소수를 구하기
    print(len([i for i in result if i>n])) #2) n보다 큰 조건만족 소수 개수구하기