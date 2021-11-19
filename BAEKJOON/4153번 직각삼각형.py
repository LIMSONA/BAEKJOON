while True:
    
    test=list(map(int,input().split()))
    test.sort() #오름차순 정렬
    
    if sum(test)==0: #0 0 0 나오면 스톱
        break
        
    #피타고라스의 정리    
    if test[0]**2 + test[1]**2 == test[2]**2:
        print('right')
    else:
        print('wrong')