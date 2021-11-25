# 토요일 집들이를 앞둔 지금!

to_do_list=['트레이더스 장보기','청소하기','음식준비하기',\
            '크리스마스 데코','가구배치하기','서울모터쇼 가기']

#어떤 조합으로 해야할까나??
from itertools import combinations
this_weekend=list(combinations(to_do_list,3))

# 집중할 3개 출력하기!
for focus in this_weekend:
    print(focus) 