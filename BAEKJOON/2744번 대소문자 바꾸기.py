target = input()
result="" #대/소문자 변경한 문자열을 받을 변수 생성

for i in range( len(target) ): #자릿 수 만큼 반복해야하므로
    
    if target[i].isupper()==True: #대문자
        result += target[i].lower()
    else: #소문자
        result += target[i].upper()
        
print(result)