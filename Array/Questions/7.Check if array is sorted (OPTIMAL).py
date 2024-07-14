
#Approach: 
#Create a max variable and initialize it with arr[0].
#Use a for loop and compare it with other elements of the array
#If any element is greater than the max value, update max value with the element’s value
#Print the max variable.

def isSorted(arr, n):
    for i in range(1,n):
        if arr[i]<arr[i-1]:
            return False
    return True

if __name__ == "__main__":
   if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = 5
    print("True" if isSorted(arr, n) else "False")
