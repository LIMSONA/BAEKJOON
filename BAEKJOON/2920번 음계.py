test=list(map(int,input().split()))
filt=[1,2,3,4,5,6,7,8]
    
if test == sorted(filt): 
    print("ascending")
elif test == sorted(filt,reverse=True):
    print("descending")
else: print("mixed")