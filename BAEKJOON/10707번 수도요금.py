# 입력은 5줄이고 한 줄에 하나씩 정수가 입력
# 첫 번째 줄에는 X사의 1리터당 요금 A
# 두 번째 줄에는 Y사의 기본요금 B
# 세 번째 줄에는 Y사의 요금이 기본요금이 되는 사용량의 상한 C
# 네 번째 줄에는 Y사의 1리터 당 추가요금 D
# 다섯 번째 줄에는 JOI군의 집에서 사용하는 한 달간 수도의 양 P
# 한 달간 수도요금을 첫째 줄에 출력

a=int(input())
b=int(input())
c=int(input())
d=int(input())
p=int(input())

x = p*a
if p<c: y=b
else: 
    y=b+(p-c)*d
    
print(min(x,y))