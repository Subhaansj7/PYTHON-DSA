

def getElements(arr, n):
    if n == 0 or n == 1:
        print(-1, -1)  # edge case when only one element is present in array
    #adding variables 
    small = float('inf')
    second_small = float('inf')
    large = float('-inf')
    second_large = float('-inf')
    #First find max and min of array 
    for i in range(n):
        small = min(small, arr[i])
        large = max(large, arr[i])
    #comparing max and min to get second max min
    for i in range(n):
        if arr[i] < second_small and arr[i] != small:
            second_small = arr[i]
        if arr[i] > second_large and arr[i] != large:
            second_large = arr[i]
    print("Second smallest is", second_small)
    print("Second largest is", second_large)



#driver code 
if __name__ == '__main__':
    arr = [1, 2, 4, 6, 7, 5]
    n = len(arr)
    getElements(arr, n)






