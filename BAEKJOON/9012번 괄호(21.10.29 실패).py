# 1차접근  -> 실패 예외 발생: ())(()
#  괄호 "(" 개수 -  ")" 개수가 0이면 y / 아니면 n

t=int(input())

for i in range(t):
    t_ex=list(input())
    a="("
    b=")"
    if t_ex.count(a) - t_ex.count(b)==0:
        print("YES")
    else:
        print("NO")
# 
# -----------------------------------------
# #2차접근  -> 이유는 모르지만 실패
# #  만약 "("라면 pop")"

t=int(input())

for _ in range(t):
    t_ex=list(input())


    for i in t_ex:
        if i=="(":
            t_ex.pop()
    print(t_ex)   

