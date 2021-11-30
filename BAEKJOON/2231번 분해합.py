# 1차시도 (실패)--------------------------
#pqr이란 수의 분해합은 100p+10q+r+p+q+r = 101p+11q+2r 구함
#규칙을 찾아보면 생성자는 (101로 나눈 몫) (11로 나눈 나눈 몫) (2로 나눈 몫)으로 구성됨
#단! 마지막에 나머지가 0으로 딱 떨어지지 않으면 (몫-1) 해줘야함


n=int(input())

a= (n//101)
a_1= n % 101 #나머지

b= a_1 // 11
b_1= a_1 % 11 #나머지

c= b_1 // 2

if b_1%2==0: print(100*a+10*b+c)

else:
    x= (n // 101) - 1
    x_1= n - (101*x) #나머지
        
    y= (x_1 // 11) - 1
    y_1= x_1 - (11*y) #나머지

    z= y_1 // 2 

    print(100*x + 10*y + z)


# 2차시도 (성공)-----------------------

n=int(input())

#숫자 반절부터 찾아보기
for sample in range(n//2,n):
    
    #각 숫자들을 더해줄 작업공간(리스트) 만들기
    workbench=[] 
    
    #샘플 숫자를 하나씩 문자열로 나눠주기
    for i in str(sample):
        workbench.append(int(i)) 
    
    #각 숫자 합과 숫자자신 더하기!
    if n == sum(workbench) + sample: 
        print(sample)
        break

#없을 경우
else: print(0)