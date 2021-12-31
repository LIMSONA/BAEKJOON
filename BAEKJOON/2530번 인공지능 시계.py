# 입력 ===========================
# 첫째 줄에는현재 시각 시,분,초  정수로 빈칸을 사이에 두고
# 두 번째 줄에는 요리하는 데 필요한 시간 초 단위
# 출력 ===========================
# 종료되는 시각의 시, 분, 초을 공백을 사이에 두고 출력

# 시작 시a 분b 초c / 걸린시간 초d
a,b,c=map(int,input().split())
d=int(input())

fin_h, fin_m, fin_s = a, b, c
# c에 조리시간 걸린 d 더하고 60넘기면 b로 
# 종료 시 fin_h / 분 fin_m / 초 fin_s
fin_s = c + d

if fin_s >=60: 
    fin_m += (c+d)//60
    fin_s = fin_s % 60

# 분단위b 60넘으면 a로 
if fin_m >=60:
    fin_h += fin_m//60
    fin_m = fin_m % 60
    
# 시단위 24넘는지 확인
if fin_h >=24: 
    fin_h = fin_h % 24
 
#종료시각 출력
print(fin_h, fin_m, fin_s)