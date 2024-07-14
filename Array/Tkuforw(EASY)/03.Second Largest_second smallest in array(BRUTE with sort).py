#Approach:
#Sort the array in ascending order
#The element present at the second index is the second smallest element
#The element present at the second index from the end is the second largest element
def getElements(arr, n):
    if n == 0 or n == 1:
        print(-1, -1)  # edge case when only one element is present in array
    arr.sort()
    small = arr[1]
    large = arr[n-2]
    print("Second smallest is", small)
    print("Second largest is", large)




if __name__ == '__main__':
    arr = [1, 2, 4, 6, 7, 5]
    n = len(arr)
    getElements(arr, n)
