n=int(input())

fib=[0,1]

for i in range(2,n+1):
    fib.append(fib[i-1]+fib[i-2])

print(fib[n])

# -------------------------

def fibo(x):
    if x==1 or x==2:
        return 1
    else:
        return fibo(x-1)+fibo(x-2)   
     
print(fibo(n))