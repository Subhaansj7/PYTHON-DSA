#SELECTION SORT  


A = [64,25,12,22,11]

#traverse through all elemts in array 
for i in range(len(A)-1):
    
    #find the minimum value element in array
    #unsorted array 
    min_idx=i
    for j in range(i+1,len(A)):
        if A[min_idx] > A[j]:
            min_idx = j 
            
    #Swap the founded min with the first element
    A[i],A[min_idx]=A[min_idx],A[i]
    
#Driver code 
print("Sorted array: ")
for i in range(len(A)):
    print(A[i],end=" ")