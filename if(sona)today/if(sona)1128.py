from collections import deque

#2020yr 좋아하는 차
my_favorite_car = [['BMW_MINI_COOPER', 'HYUNDAI_NEXO', 'GENESIS_GV80']]
in_my_mind = deque(my_favorite_car)

#2021 서울모빌리티 가기 전
these_days=[['HYUNDAI_CASPER', 'BMW_IX', 'PORSCHE_TARGA'],\
#2021 서울 모빌리티 갔다 온 후
            ['MERCEDES_BENZ_EQS']]

for i in these_days:
    in_my_mind.append(i)
    in_my_mind.popleft()
    
    print('요즘 my_favorite_cars는', in_my_mind)
