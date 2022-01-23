# 0이 있다는 거면 10이라는 것
# 2자리면 각자리 더하면 됨,
# 3자리면 10이있다는 것,
# 4자리면 둘다 10

num=str(input())

if len(num)==2 : print(int(num[0]) + int(num[1]))
elif len(num)==4: print(20)
else: 
    if num[1]=='0': print(int(num[:2]) + int(num[2]))
    else: print(int(num[0])+ int(num[1:]))