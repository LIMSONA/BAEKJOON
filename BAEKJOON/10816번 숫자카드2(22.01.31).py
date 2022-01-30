n= int(input()) #상근이가 가지고 있는 숫자 카드의 개수
cards= list(map(int,input().split())) #숫자 카드에 적혀있는 정수
m= int(input()) 
test= list(map(int,input().split()))

dic= {}

for i in cards:
    dic[i] = dic.get(i, 0) + 1

for i in test:
    if i in dic: print(dic[i], end=" ")
    else: print(0, end=" ")


# 시간초과 실패===========================
# n= int(input()) #상근이가 가지고 있는 숫자 카드의 개수
# cards= list(map(int,input().split())) #숫자 카드에 적혀있는 정수
# m= int(input()) 
# test= list(map(int,input().split()))


# for i in test:
#     result = cards.count(i)
#     print(result,end=" ")

# from sys import stdin,stdout
# n= int(stdin.readline())
# cards= list(map(int,stdin.readline().split())) #숫자 카드에 적혀있는 정수
# m= int(input()) 
# test= list(map(int,stdin.readline().split()))


# for i in test:
#     result = cards.count(i)
#     stdout.write(result,end=" ")

