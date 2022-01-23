n=int(input())

# 1+8d 규칙으로 엄지손가락
# 나머지 1검지 2중지 3약지 4종지 5약지 6중지 7검지 0엄지
# 검지는 1번 / 중지는 2번 / 약지는 3번 / 종지는 4번
problem=[1,2,3,4,5,4,3,2]


if n==1: print(1) #엄지
else:
    ind=(n-1)%8
    print(problem[ind])
    