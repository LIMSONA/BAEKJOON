#업그레이드 소수 알고리즘

def sosu_upgrade(x):    #약수의 성질을 이용한 개선 소수알고리즘
    if x==1:
        return False    #논외 대상이니 False
    else:
        for i in range(2,int(x**(1/2))+1):   #나누는 것은 2부터~x제곱근까지로 나눠야함.
            if x%i==0:  
                return False    #나눠 떨어지니까 False
        return True #다른 것들은 True
                   
m, n = map(int,input().split())

for i in range(m,n+1):
    if sosu_upgrade(i):
        print(i)