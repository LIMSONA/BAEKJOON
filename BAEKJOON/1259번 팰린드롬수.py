#팰린드롬 앞뒤가 똑같은 것

while True:
    test= input()
    if test=='0': 
        break
    else:
        if test==test[::-1]:
            print("yes")
        else:
            print("no")
