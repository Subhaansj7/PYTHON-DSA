#APPEND()

# importing "array" for array operations
import array

#initializing array with array values and signed integers
arr = array.array('i', [1, 2, 3]) 

# using append() to insert new value at end
arr.append(4);

# printing appended array
print("The appended array is : ", end="")
for i in range (len(arr)):
    print (arr[i], end=" ")
    
    
#Array insert(i,x) Method in Python


arr.insert(2, 5)



#array pop() Method in Python


# using pop() to remove element at 2nd position
print ("The popped element is : ",end="")
print (arr.pop(2));
 
 
#Array remove() in Python


arr.remove(1)


#Array index() Method

print (arr.index(2))

#Array reverse() Function

arr.reverse()