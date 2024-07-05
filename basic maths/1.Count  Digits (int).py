#normal
number=int(input("Enter number: "))


count=0
while number != 0:
    number = number // 10
    count = count+1
    
print("count : ",count)



#within function

def digit_counter(number):
    count = 0
    while number != 0:
        number = number// 10
        count = count + 1
        
    return count
    
print("count : ",digit_counter(412356))


#If int is Negative

def digit_counter(number):
    number=abs(number)
    count = 0
    while number != 0:
        number = number// 10
        count = count + 1
        
    return count
    
print("count : ",digit_counter(412356))



# if int = 0 

def digit_counter(number):
    number=abs(number)
    count = 0
    if number == 0:
        pass
    else:
         while number != 0:
             number = number// 10
             count = count + 1
         
    return count
    
   
print("count : ",digit_counter(412356))


