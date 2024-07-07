num1=int(input("ENTER NO 1 :"))
num2=int(input("ENTER NO 2 :"))

if num1>num2:
    mn=num2
else:
    mn=num1
    
    
for i in range(1,mn+1):
    if num1%i==0 and num2%i==0:
         hcf=i
   
    
print(f"the HCF?GDC of numbers {num1} and {num2} is :  {hcf}")