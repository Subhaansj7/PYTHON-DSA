#Approach: 

#Declare a HashSet.
#Run a for loop from starting to the end.
#Put every element of the array in the set.
#Store size of the set in a variable K.
#Now put all elements of the set in the array from the starting of the array.
#Return K.
def removeDuplicates(arr):
    st=set()
    for i in range(len(arr)):
        st.add(arr[i])
    k=len(st)
    j=0
    for x in st:
        arr[j]=x
        j=j+1 
    return k

if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 3, 3]
    k = removeDuplicates(arr)
    print("The array after removing duplicate elements is ")
    for i in range(k):
        print(arr[i], end=" ")
