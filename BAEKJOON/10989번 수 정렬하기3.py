# n=int(input())
# num=[]
# for _ in range(n):
#     inp=int(input())
#     num.append(inp)
#     num.sort()
# for i in num:
#     print(i)



import sys 

n=int(sys.stdin.readline())  #첫째 줄 n개가 주어짐
num=[0]*10001                #입력 수들이 10,000이하/ 0부터 시작하는 리스트는 10,001개를 만들어야 함
for _ in range(n):
    test=int(sys.stdin.readline())   #입력 수들을 정수로 받고
    num[test]+=1                     #입력된 정수의 리스트 자리에는 하나씩 카운트하여 나온 횟수 체크

#이제 리스트에서 하나씩 꺼내서 출력
for i in range(10001):               #리스트가 (0~10,000) 10,001번 반복해서 빼오면
    if num[i] !=0:                   #0인 경우엔 없으니 출력할 필요없고, 0이 아닌 경우만 출력
        for _ in range(num[i]):      #카운트 횟수인 리스트 각 자리만큼 반복 
            print(i)               