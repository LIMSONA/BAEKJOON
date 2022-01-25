# 주사위 30개를 10000번 던졌을때 합 정규 분포표
import matplotlib.pyplot as plt
import random

second=[0]*(6*30+1) #30개 주사위로 던졌을 때 합의 경우의 수 

for _ in range(10000):
    first=[]        
    for _ in range(30):
        dice=random.randint(1,6)
        first.append(dice)
    
    a=sum(first) # 30개 주사위로 1회 던진 값의 합
    second[sum(first)]+=1 #경우의 수에 1씩 count 추가

result2=[]
for i in second:
    result2.append(i/10000) #확률로 봐야하니까 나눠주기


plt.bar(range(30,181),result2[30:])
plt.plot(range(30,181),result2[30:])
plt.show()

