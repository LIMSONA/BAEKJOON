# sona 하루의 소소한 실천에서 시작하는 푸른 하늘 대작전

def sona(day):
    
    #오늘부터 인생의 마지막 날까지 
    if day==the last day of my life:
        return
    
    #온난화를 위한 작은 실천으로
    sys.stdout.write(day, '번 실내 적정온도를 유지했습니다')
    sys.stdout.write(day, '번 재활용을 올바르게 분리배출 했습니다')
    
    sona(day + 1)
    
    #나의 작은 실천으로 푸른 하늘을 볼 수 있는 날들을 출력
    #마지막 날 이후 실천이 없어서, 푸른 하늘을 볼 수 있는 날이 감소 
    sys.stdout.write(day, '번 푸른하늘을 볼 수 있습니다')

#오늘부터 시작되는 실천
sona(today)
