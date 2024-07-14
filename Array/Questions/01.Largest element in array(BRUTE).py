#Approach: 
#Sort the array in ascending order.
#Print the (size of the array -1)th index.
#DryRun: 
#Before sorting: arr[] = {2,5,1,3,0};

#After sorting: arr[] = {0,1,2,3,5};

#Hence answer : arr[sizeofthearray-1] =5

from typing import List
def sortArr(arr: List[int]):
    arr.sort()
    return arr[-1]
if __name__ == "__main__":
    arr1 = [2, 5, 1, 3, 0]
    arr2 = [8, 10, 5, 7, 9]
    print("The Largest element in the array is:", sortArr(arr1))
    print("The Largest element in the array is:", sortArr(arr2))
