#Approach:
#We would require four variables: small,second_small, large, and second_large. Variable small and second_small are initialized to INT_MAX while large and second_large are initialized to INT_MIN.
#
#Second Smallest Algo:

#If the current element is smaller than ‘small’, then we update second_small and small variables
#Else if the current element is smaller than ‘second_small’ then we update the variable ‘second_small’
#Once we traverse the entire array, we would find the second smallest element in the variable second_small.
#Here’s a quick demonstration of the same.
#Second Largest Algo:

#If the current element is larger than ‘large’ then update second_large and large variables
#Else if the current element is larger than ‘second_large’ then we update the variable second_large.
#Once we traverse the entire array, we would find the second largest element in the variable second_large.
#Here’s a quick demonstration of the same.///


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
