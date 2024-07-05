

print("ENter the number: ")
number=int(input())
temp = number
reverse = 0

while number != 0:
    last_digit= number % 10
    reverse = reverse * 10 + last_digit
    number = number // 10
    
if temp == reverse:
    print("The int is palindrome")

else:
    print("The int is not palindrome")