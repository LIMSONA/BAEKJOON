# 문자열의 첫 글자와 마지막 글자

num= int(input())

for _ in range(num):
    test=input()
    print(test[0], #첫 글자
          end="") #첫 글자와 마지막 글자 이어서 출력 
    print(test[-1]) #마지막 글자