def lowerBound(arr,n,x):
    low=0
    high=n-1
    ans=n 
    
    while low<=high:
        mid = (low + high)//2
        #may be answer
        if arr[mid] >= x:
            ans = mid
            #look for smaller index on left 
            high = mid -1 
        else:
            low = mid + 1 #look on right
    return ans 
            
#driver code
if __name__ == "__main__":
    arr = [3, 5, 8, 15, 19]
    n = 5
    x = 16
    ind = lowerBound(arr, n, x)
    print("The lower bound is the index:", ind)