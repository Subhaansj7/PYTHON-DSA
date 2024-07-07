number=int(input("enter no: "))

def div(n):
    divisors=0
    for i in range(1,n//2+1):
        if n % i == 0:
            divisors=divisors+1
    
    return divisors+1

div(number)