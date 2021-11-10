# m이상 n이하 소수를 모두 출력
# 첫재줄 자연수m,n
# 출력 한줄씩 정렬 출력

# 나머지가 0인것이 없어야함

#1. 소수 찾기 함수
#2. 반복문 통해 m~n사이 숫자들을 소수찾기 함수를 돌려서 출력

def sosu(x):
    i=2 #나누는 값 i (2부터 나누기 시작)
    while i != x: #나누는 값이 x값과 같으면 반복문 중단
        if x%i==0: #나머지가 0 (소수 아님)
            break
        else: #나머지가 0아님 (소수 가능성)
            if i==x-1:  #가장 마지막까지 돌렸는데도 나머지 0이 없는 경우
                return print(x)
            else:   #나누는 수에 증가시킬수 있는 경우
                i+=1        
    return


def sosu_not(x):    #소수가 아닌 것 찾는 함수로
    if x==1:
        return False    #논외 대상이니 False
    else:
        for i in range(2,x):    #나누는 것은 2부터~(x-1)까지로 나눠야함.
           if x%i==0:
               return False     #나눠 떨어지니까 False
        return True     #다른 것들은 True
    
                   
m, n = map(int,input().split())

for i in range(m,n+1):
    if sosu_upgrade(i):
        print(i)
    
    

