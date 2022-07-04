# 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로
# 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로
# 행렬의 원소는 절댓값이 100보다 작거나 같은 정수

#n,m 열,행 입력받기
n,m = map( int, input().split() )

#A,B 행렬 입력받기
A,B= [],[] 
for _ in range(n): #n개줄
    A.append(list(map(int,input().split())))    
for _ in range(n): #n개줄
    B.append(list(map(int,input().split())))

#이중리스트 덧셈 더하기
for i in range(n):
    X,Y = A[i],B[i] #한 행씩 더하도록
    result= [ X[j]+Y[j] for j in range(m)] # 더하는 것은 열(m) 개수만큼 진행됨    
    print( " ".join(map(str, result)) ) # 각 값이 공백으로 출력 - join은 문자열만 사용가능하므로!



# a=[0,0,0]
# b=[1,2,3]
# print(a+b)  출력 [0, 0, 0, 1, 2, 3]
# print([a[i]+b[i] for i in range(len(a))]) 출력 [1, 2, 3]