# 뉴비: 1학년 or 2학년
# 올드비: n학년 이하 and 뉴비 아님
# 틀리: 뉴비 아님 and 올드비 아님

n,m=map(int,input().split())



if m==1 or m==2: print("NEWBIE!")
else: 
    if m<=n: print("OLDBIE!")
    else: print("TLE!")