#Algorithm:
#First, using a loop, we will place the pointer j. If we don’t find any 0, we will not perform the following steps.
#After that, we will point i to index j+1 and start moving the pointer using a loop.
#While moving the pointer i, we will do the following:
#If a[i] != 0 i.e. a[i] is a non-zero element: We will swap a[i] and a[j]. 
#Now, the current j is pointing to the non-zero element a[i].
#So, we will shift the pointer j by 1 so that it can again point to the first zero.
#Finally, our array will be set in the right manner.

def moveZeros(n,arr):
    j = -1
    # Place the pointer j
    for i in range(n):
        if arr[i] == 0:
            j = i
            break
    
    # No non-zero elements
    if j == -1:
        return arr
    
    # Move the pointers i and j and swap accordingly
    for i in range(j + 1, n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    
    return arr


arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
n = 10
ans = moveZeros(n, arr)
for it in ans:
    print(it, end=' ')
print()