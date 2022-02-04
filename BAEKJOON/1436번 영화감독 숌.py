n= int(input()) # 몇번째 수를 보길 원하는지 입력받기

cnt= 0 # 666이 들어가는 수 中 몇번째인지 카운트
start= 666 # 가장 작은수는 666이니까
while True:
    # 666이 들어가있는지 문자열변환 후 확인하고, 맞으면 cnt에 +1
    if '666' in str(start):
        cnt+=1
    # cnt 카운트 수와 원하는 n과 같으면 출력 후 break
    if cnt == n:
        print(start)
        break
    
    # 하나씩 숫자를 키워가면서 확인한다
    # ex) 666에 1씩 더해가면서 커지는 중~
    start+=1