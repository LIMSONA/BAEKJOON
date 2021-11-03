t = int(input())
for i in range(t):
    floor = int(input())
    room = int(input())

    base = [j for j in range(1, room+1)] #0층 각 호수의 인원 리스트
    
    for k in range(floor):      # 층수만큼 반복
        for n in range(1,room):    #이전리스트에다가 하나씩 덮어쓰기로 넣어서 리스트 만들기
            base[n]=base[n]+base[n-1]
    
    print(base[-1])

    
