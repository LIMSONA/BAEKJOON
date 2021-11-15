# 우선순위: 호수번호 적은거 -> 낮은 층
# 1호가 쭉 다채워지고 그다음 2호가 쭉 채워짐
# 즉, n번째는 건물층수h로 나눈 나머지가 층수, 몫+1이 호수

#t : 테스트개수
#h : 건물 층수
#w : 한층 방 개수
#n : n번째 손님
#x : n번째 손님 호수
#y : n번째 손님 층수
#답출력 yxx나 yyxx형태
 
t=int(input())

for _ in range(t):
    h,w,n=map(int,input().split())
    
    y = n % h
    x = (n//h)+1
    
    #나머지가 0인 경우 문제 생김
    #예외 예시) 6층에 건물 12번째 손님
    if y==0:    
        y=h
        x=x-1
    print(y*100+x)
    
    # 아래 방법으로도 답 출력 가능함
    # if x<10:      
    #     x='0'+str(x)
    # print(str(y)+x)