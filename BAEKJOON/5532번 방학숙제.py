#====문제에 오타가 있음====
#c가 하루최대 수학 / d가 하루최대 국어

# 놀수있는 날 최댓값 출력
# 방학일 l에서 해결걸린 수 빼서 답 구하기

l=int(input())
a=int(input()) #수학
b=int(input()) #국어
c=int(input()) #하루 수학
d=int(input()) #하루 국어

math = a//c
korean = b//d
 
if (a%c)!=0: math+=1
if (b%d)!=0: korean+=1

max_d =  max(math,korean)
print(l-max_d)