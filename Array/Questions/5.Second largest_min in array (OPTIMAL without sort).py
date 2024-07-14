


def secondSmallest(arr, n):
    if (n < 2):
        return -1 # edge case when only one element is present in array
    #adding variables 
    small = float('inf')
    second_small = float('inf')
    # min to get second min and comparing each elemeng
    for i in range(n):
        if (arr[i] < small):
            second_small = small
            small = arr[i]
        elif (arr[i] < second_small and arr[i] != small):
            second_small = arr[i]
    return second_small




def secondLargest(arr, n):
    if (n < 2):
        return -1 # edge case when only one element is present in array
    #adding variables 
    large = float('-inf')
    second_large = float('-inf')
    # max to get second max and comparing each elemeng
    for i in range(n):
        if (arr[i] > large):
            second_large = large
            large = arr[i]
        elif (arr[i] > second_large and arr[i] != large):
            second_large = arr[i]
    return second_large




if __name__ == "__main__":
    arr = [1, 2, 4, 7, 7, 5]
    n = len(arr)
    sS = secondSmallest(arr, n)
    sL = secondLargest(arr, n)
    print("Second smallest is", sS)
    print("Second largest is", sL)