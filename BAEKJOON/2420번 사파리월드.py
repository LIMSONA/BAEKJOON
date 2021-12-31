# 유명도는 정수그 차이를 구하는 프로그램을 작성
# 첫째 줄에 두 유명도의 차이 (|N-M|)을 출력 

# => 절대값을 출력하는 거니까 abs!!

a,b= map(int,input().split())

print(abs(a-b))