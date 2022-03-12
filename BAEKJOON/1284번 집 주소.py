# 각 숫자 사이에는 1cm의 여백이 들어가야한다.
# 1은 2cm의  / 0은 4cm의 / 나머지 숫자는 모두 3cm의 너비를 차지
# 호수판의 경계와 숫자 사이에는 1cm의 여백이 들어가야한다.


while True : 
    ad = str(input())
    if ad == '0': break
    else: 
        # 조건 설정해주기
        def cal(x):
            if x == "0": return 4
            elif x == "1": return 2
            else: return 3

        #숫자 계산하기    
        tmp=0
        for i in ad:
            tmp += cal(i)
        #숫자 + 양쪽 + 숫자간격
        result = tmp + 2 + ( len(ad) - 1 )

        print(result) 