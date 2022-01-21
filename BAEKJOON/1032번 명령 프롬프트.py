#==============성공!
# 1/2/3이 있다면,
# 1과2를 먼저 비교 그다음에 그 결과랑 3과 비교

t=int(input())
 
before = list(input())
for i in range(t-1):
    after = list(input())
    for j in range(len(before)):
        if before[j] != after[j]: before[j]="?"
print("".join(before))

#===============실패!
# t=int(input())
# if t==1: print(input())
# else:
#     a=[]
#     for i in range(t):
#         file = input()
#         a.append(file)
    
#     cnt=0
#     sentence="a[0][i]"
#     for i in range(t-1):
#         sentence+="=="
#         cnt+=1
#         sentence+="a["+str(cnt)+"][i]"
#     print(sentence)    
        
#     result=""    
#     for i in range(len(a[0])):
#         #0부터 len(n)-1까지 일치하는지
#         if sentence: 
#             result=result+(a[0][i])
#         else:
#             result=result+"?"
            
#     print(result)