pos = -1

def search(arr,n):
    i = 0
    
    while i < len(arr):
        if arr[i]==n:
            globals()['pos']=i
            return True
        i=i+1 
    return False
                
                
arr=[4,7,8,12,45,99]
n=45

if search(arr,n):
    print("Found at",pos)
else:
    print("Not Found")