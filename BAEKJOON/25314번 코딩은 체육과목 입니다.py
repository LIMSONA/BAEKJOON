n= int(input())

for _ in range(int(n/4)): # 4로 나눈 값 만큼 반복
    print("long ",end="") #이어서 출력
print("int")

# 다른 방법===================
n= int(input())

print("long "* int(n/4),end="")
print("int")