from collections import deque

my_favorite_car = [['BMW_MINI_COOPER', 'HYUNDAI_NEXO', 'GENESIS_GV80']]
in_my_mind = deque(my_favorite_car)

these_days=[['HYUNDAI_CASPER', 'BMW_IX', 'PORSCHE_TARGA'],\
            ['MERCEDES_BENZ_EQS']]

for i in these_days:
    in_my_mind.append(i)
    in_my_mind.popleft()
    
    print('my_favorite_cars는', in_my_mind)
