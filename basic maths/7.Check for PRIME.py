number=int(input("enter no: "))

if number==1:
    print ("not prime")
if number>1:
    for i in range(2,number+1):
         if number%i==0:
             print("not prime")
             break
    else:
       print("prime")
    
    
