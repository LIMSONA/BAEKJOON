# 세 각의 크기가 모두 60이면, Equilateral
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
# 세 각의 합이 180이 아닌 경우에는 Error

a = int(input())
b = int(input())
c = int(input())

if a+b+c==180:
    # 세 각의 크기가 모두 60이면, Equilateral
    if a==b==c==60: print("Equilateral")
    # 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
    elif a==b or b==c or c==a: print("Isosceles")
    # 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
    else: print("Scalene")

# 세 각의 합이 180이 아닌 경우에는 Error
else: print("Error") 