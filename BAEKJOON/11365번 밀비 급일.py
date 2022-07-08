while True: #while 반복문을 통해 계속 입력받고
    a= input() # 입력 받고
    if a=="END": #이 경우는 break로 멈추고
        break
    else:
        print(a[::-1]) 
        #입력받은 문자열을 맨 뒤에서부터 하나씩 출력