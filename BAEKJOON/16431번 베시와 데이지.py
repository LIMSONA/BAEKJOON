# b직사각형 정사각형 자르고 그만큼 수직수평
# d 수직수

b1,b2=map(int,input().split()) #베시
d1,d2=map(int,input().split()) #데이지
j1,j2=map(int,input().split()) #존



# 베시
x= abs(j1-b1)
y= abs(j2-b2)
if min(x,y)==0:
    bessie = max(x, y)
else:
    # 대각선길이
    if x==y: bessie=x
    # 대각선과 남은 길이
    else: bessie = min(x, y) + (max(x, y) - min(x, y))

# 데이지
daisy = abs(j1- d1) + abs(j2-d2)



if daisy==bessie: print("tie")
elif daisy>bessie: print("bessie")
elif daisy<bessie: print("daisy")