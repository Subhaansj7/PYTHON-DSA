number=int(input("enter num: "))

def reverse(n):
    if n<10:
        return n
    else:
        return int(str(n%10)+str(reverse(n//10)))


def ispalindrome(n):
    if number==reverse(n):
        return 1
    return 0
    
if ispalindrome(number)==1:
    print("Palindrome")
else:
    print("not a Palindrome")