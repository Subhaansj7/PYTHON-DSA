#Linear Search in Python


def linearSearch(array, n, num):

    # Going through array sequencially
    for i in range(0, n):
        if (array[i] == num):
            return i
    return -1


array = [2, 4, 0, 1, 9]
num = 1
n = len(array)
result = linearSearch(array, n, num)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)