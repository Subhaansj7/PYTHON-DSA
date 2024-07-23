pos = -1

def search(arr,n):
    l=0
    u=len(arr)-1
    
    while l<=u:
        mid = (l+u)//2
        
        if arr[mid] == n:
            globals()['pos']=mid
            return True
        else:
            if arr[mid]<n:
                l=mid
            else:
                u=mid
                
                
arr=[4,7,8,12,45,99]
n=45

if search(arr,n):
    print("Found at",pos)
else:
    print("Not Found")