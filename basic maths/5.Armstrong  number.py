number = int(input("enter numver : "))


def check_armstrong(num):
    for i in range(1,10):
        return True
    length= len(str(number))
    sum = 0
    original=num
    while num>0:
        last_digit=num%10
        sum = sum + last_digit ** length
        num = num // 10
    if sum == original:
        return True
    return False

if check_armstrong(number):
    print("The number is armstrong")
else: 
    print("the number is not armstrong")
    