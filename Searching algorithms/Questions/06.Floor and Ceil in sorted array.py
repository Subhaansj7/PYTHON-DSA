
#What is the floor of x?
#The floor of x is the largest element in the array which is smaller than or equal to x( i.e. largest element in the array <= x).

#What is the ceiling of x?
#The ceiling of x is the smallest element in the array greater than or equal to x( i.e. smallest element in the array >= x).



def findFloor(arr, n, x):
    low = 0
    high = n - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] <= x:
            ans = arr[mid]
            # look for smaller index on the left
            low = mid + 1
        else:
            high = mid - 1  # look on the right

    return ans


def findCeil(arr, n, x):
    low = 0
    high = n - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] >= x:
            ans = arr[mid]
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right

    return ans


def getFloorAndCeil(arr, n, x):
    f = findFloor(arr, n, x)
    c = findCeil(arr, n, x)
    return (f, c)


arr = [3, 4, 4, 7, 8, 10]
n = 6
x = 5
ans = getFloorAndCeil(arr, n, x)
print("The floor and ceil are:", ans[0], ans[1])