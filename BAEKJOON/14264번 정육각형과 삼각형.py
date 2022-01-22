t=int(input())
# 2:1:3**2 = L:x:y  =====> 답은 x*y

print( (0.5*t) * (3**0.5)*(0.5*t) )

# 동일식 제곱근의 경우 math 모듈 사용해서 구하기
# import math
# print( (0.5*t) * (math.sqrt(3))*(0.5*t) )
