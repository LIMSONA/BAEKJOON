# # M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 
# # 둘째 줄에 그 중 최솟값을 출력한다. 
# # 단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.

# 어떤 수를 1~n까지 넣어서 
# (1과 n으로 나눈건..... 나머지 0이니 빼고 2~n-1까지)
# 나눠서 나머지가 0이 나왔으면 그건 소수가 아님
# 그 나머지의 경우 소수



m=int(input())
n=int(input())
a=[]
for i in range(m,n+1):
    if i == 1:
        pass
    elif i == 2:
        a.append(i)
    else:
        for j in range(2, i):
            if i % j == 0:
                break
            elif j == i-1:      #가장 마지막에서 i를 추가
                a.append(i)

if len(a)==0:
    print(-1)
else:
    print(sum(a))
    print(min(a))





# m = int(input())
# n = int(input())
# a = []

# def sona(x):
#     for i in range(2,x):
#         if x%i==0:
#             return #소수가 아닙니다!
#     return a.append(x)   #소수입니다!

# for i in range(m, n+1):
#     sona(i)
    
# # print(a)
# print(sum(a))
# print(min(a))

# # a=list()
# # for i in range(1,10):
# #     a.append(sona(i))
# #     print(a)


