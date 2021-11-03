c = int(input())
for j in range(c):
    case =list(map(int,input().split(" ")))

    avg=sum(case[1:])/case[0]
    cnt=0
    for i in case[1:]:
        if i>avg:
            cnt+=1

    result=cnt/case[0]*100

    print("%.3f"%result+"%")

# print(sum(case[1:-1])/case[0]*100)

# total = int(input())

# for i in range(total):
#     case = list(map(int, input().split(" ")))

#     #avg = sum(case[1:])/case[0]
#     print("%.3f"%(sum(case[1:])/case[0]) + "%")