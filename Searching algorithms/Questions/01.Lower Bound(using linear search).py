#What is Lower Bound?
#The lower bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than 
#or equal to a given key i.e. x.
#The lower bound is the smallest index, ind, where arr[ind] >= x. 
#But if any such index is not found, the lower bound algorithm returns n i.e. size of the given array.

def lowerBound(arr,n,x):
    for i in range(n):
        if arr[i]>=x:
            #lower bound found
            return i 
    return n 
        

#driver code
if __name__ == "__main__":
    arr = [3, 5, 8, 15, 19]
    n = 5
    x = 9
    ind = lowerBound(arr, n, x)
    print("The lower bound is the index:", ind)