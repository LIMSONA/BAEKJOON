#소수 판별 알고리즘-------------------------

def sosu(x):
    for i in range(2,x):    #1과 자기자신 제외하는 범위
        
        #조건: i로 나누면 나누어떨어짐
        if x % i == 0:   
            return '소수 X'
   
    return '소수 O'

print(sosu(4))    #소수 X 출력
print(sosu(7))    #소수 O 출력


#업그레이드 소수 판별 알고리즘-----------------

import math

def sosu_upgrade(x):
    
    for i in range(2, int(math.sqrt(x))+1):
        
        #조건: i로 나누면 나누어떨어짐
        if x % i == 0:   
            return '소수 X'
        
    return '소수 O'