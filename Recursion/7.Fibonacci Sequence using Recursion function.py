def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-2)+fib(n-1)

print(fib(8))

#or for loop to look whole sequence

for n in range(0,16):
    print(fib(n),end=" ")