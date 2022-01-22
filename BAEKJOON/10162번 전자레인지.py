# 버튼 A, B, C에 지정된 시간은 각각 5분, 1분, 10초
# 요리해야할 시간 T가 초단위로 표시
# 단 버튼 A, B, C를 누른 횟수의 합은 항상 최소
# 첫 줄에 차례대로 출력해야 한다. 횟수 사이에는 빈 칸을 둔다.
# 제시된 3개의 버튼으로 T초를 맞출 수 없으면 음수 -1을 첫 줄에 출력

# [방법1]=============================    
subject=int(input())
if subject%10 !=0: print(-1)
else:
    x=y=z=0
    while subject>0:
        if subject>=300:
            x+=1 
            subject-=300
        elif subject>=60:
            y+=1
            subject-=60
        elif subject>=10:
            z+=1
            subject-=10

    print(x,y,z)


# [방법2]========================== 
subject=int(input())

if subject%10 !=0: print(-1)
else:
    x=y=z=0
    x= subject//300
    y= (subject%300)//60
    z= ((subject%300)%60)//10
    print(x,y,z)


