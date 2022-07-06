while True:
    m,n= map(int, input().split()) # 정수 입력받기
    if m==0 and n==0: # 둘다 0 0이면
        break
    elif m > n:  # 첫번째 수 크면
        print("Yes")
    else:        # 첫번째 수 작으면
        print("No")
        
        
#======== 다른 방법 =========       
        
while True:
    a,b = map(int,input().split())
    if a==0 and b==0:
        break
    print("Yes" if a > b else "No")        
