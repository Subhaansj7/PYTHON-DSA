#within function
def number_reverse(number):
    reverse=0
    temp=number
    while temp != 0:
        last_digit= temp % 10
        reverse = reverse * 10 +last_digit
        temp = temp // 10
    return reverse
    

print("Revrese of the number ",number_reverse(54231))




#Normal
number= int(input("enter the number: "))

reverse=0
temp=number
while temp != 0:
    last_digit= temp % 10
    reverse = reverse * 10 +last_digit
    temp = temp // 10
print("reverse of the number is : ",reverse)