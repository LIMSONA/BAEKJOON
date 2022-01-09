# 첫 번째 줄에는 과자 한 개의 가격 K, 
# 사려고 하는 과자의 개수 N, 
# 현재 동수가 가진 돈 M

k,n,m = map(int,input().split())

result = k*n-m

if result >=0: print(result)
else: print(0)