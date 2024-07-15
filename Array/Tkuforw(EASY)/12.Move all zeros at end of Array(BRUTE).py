#Algorithm:
#Suppose, there are N-X zeros and X non-zero elements in the array. 
#We will first copy those X non-zero elements from the original array to a temporary array. 
#Then, we will copy the elements from the temporary array one by one and fill the first X places of the original array. 
#The last N-X places of the original array will be then filled with zero. Now, our task is completed.


def moveZeros(n,arr):
    # Temporary array
    temp = []
    
    # Copy non-zero elements from original to temp array
    for i in range(n):
        if arr[i] != 0:
            temp.append(arr[i])
    
    # Number of non-zero elements
    nz = len(temp)
    
    # Copy elements from temp to fill first nz fields of original array
    for i in range(nz):
        arr[i] = temp[i]
    
    # Fill the rest of the cells with 0
    for i in range(nz, n):
        arr[i] = 0
    
    return arr

arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
n = 10
ans = moveZeros(n, arr)
for it in ans:
    print(it, end=" ")
print()

