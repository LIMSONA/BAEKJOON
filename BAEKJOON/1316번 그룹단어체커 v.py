# # 나중에 다른 알파벳뒤 한번더 나오면 그룹단어가 아님
# 어떤 자리 뒤로 같은거 있는지 묻기
# 1.연속O 
# 1-1)다음자리도 연속인지 물어보고
# 1-2)어느순간 뒤에 다른거 나오면, 그 다른숫자 다음으로 자기가 포함되어 있는지
# 포함되어 있으면 그룹단어가 아님 

# 2. 연속x 
# 이후로 자기가 포함되어 있는지



# A. 그룹단어를 출력하시오

# n=int(input())

# for _ in range(n):
#     t=list(input())
#     for i in range(len(t)):
#         if t[i]!=t[i+1]:
#             if t[i] in t[i+1:]:
#                print("그룹단어 아님")
            
#         else:
#                 print("그룹단어임")
#                 pass


n=int(input())
for _ in range(n):
    t=list(input())

    for i in range(0,len(t)):
        if t[i]==t[i+1]:
            pass
        else:
            if t[i] in t[i+1:]:
                n-=1
        break
    print(n)
        