#What is Upper Bound?
#The upper bound algorithm finds the first or the smallest index in a sorted array where the value at that index is 
#greater than the given key i.e. x.
#The upper bound is the smallest index, ind, where arr[ind] > x.
#But if any such index is not found, the upper bound algorithm returns n i.e. size of the given array. 
#The main difference between the lower and upper bound is in the condition. 
#For the lower bound the condition was arr[ind] >= x and here, in the case of the upper bound, it is arr[ind] > x.

def upperBound(arr,x,n):
    for i in range(n):
        if arr[i] > x:
            # upper bound found
            return i
    return n

if __name__ == "__main__":
    arr = [3, 5, 8, 9, 15, 19]
    n = 6
    x = 9
    ind = upperBound(arr, x, n)
    print("The upper bound is the index:", ind)
