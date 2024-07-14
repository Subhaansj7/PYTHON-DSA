#Approach: 
#Create a max variable and initialize it with arr[0].
#Use a for loop and compare it with other elements of the array
#If any element is greater than the max value, update max value with the element’s value
#Print the max variable.

def largestElement(arr,n):
    max=arr[0]
    for i in range(0,n):
        if max < arr[i]:
            max = arr[i]
    
    return max

if __name__ == "__main__":
    arr1 = [2, 5, 1, 3, 0]
    n = 5
    max = largestElement(arr1, n)
    print("The largest element in the array is:", max)


    arr2 = [8, 10, 5, 7, 9]
    n = 5
    max = largestElement(arr2, n)
    print("The largest element in the array is:", max)
