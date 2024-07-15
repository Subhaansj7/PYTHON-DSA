#Approach:
#Take two pointers let’s say i,j pointing to the 0th index of arr1 and arr2.
#Create an empty vector for storing the union of arr1 and arr2.
#From solution 2 we know that the union is nothing but the distinct elements in arr1 + arr2 
#Let’s traverse the arr1 and arr2 using pointers i and j and insert the distinct elements found into the union vector.
#While traversing we may encounter three cases.

#arr1[ i ] == arr2[ j ] 
#Here we found a common element, so insert only one element in the union. Let’s insert arr[i] in union and increment i.

#NOTE: There may be cases like the element to be inserted is already present in the union, in that case, we are inserting duplicates which is not desired.
#So while inserting always check whether the last element in the union vector is equal or not to the element to be inserted. 
#If equal we are trying to insert duplicates, so don’t insert the element, else insert the element in the union. 
#This makes sure that we are not inserting any duplicates in the union because we are inserting elements in sorted order.
#arr1[ i ]  < arr2[ j ]
#arr1[ i ] < arr2[ j ] so we need to insert arr1[ i ] in union.
#IF last element in  union vector is not equal to arr1[ i ],then insert in union else don’t insert.
#After checking Increment i.
#arr1[ i ] > arr2[ j ]
#arr1[ i ] > arr2[ j ] so we need to insert arr2[ j ] in union. 
#IF the last element in the union vector is not equal to arr2[ j ], then insert in the union, else don’t insert.
#After checking Increment j. After traversing if any elements are left in arr1 or arr2 check for condition and insert in the union.

def find_union(arr1, arr2):
    i, j = 0, 0  # Pointers
    union = []  # Union list

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:  # Case 1 and 2
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        else:  # Case 3
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1

    while i < len(arr1):  # If any elements left in arr1
        if union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    while j < len(arr2):  # If any elements left in arr2
        if union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    return union


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

union = find_union(arr1, arr2)

print("Union of arr1 and arr2 is:")
print(*union)