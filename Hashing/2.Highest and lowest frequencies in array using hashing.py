# Python code to find the difference between highest 
# and least frequencies 
 
from collections import defaultdict
def findDiff(arr,n):
 
    # Put all elements in a hash map
    mp = defaultdict(lambda:0)
    for i in range(n):
        mp[arr[i]]+=1
 
    # Find counts of maximum and minimum 
    # frequent elements 
    max_count=0;min_count=n
    for key,values in mp.items():
        max_count= max(max_count,values)
        min_count = min(min_count,values)
 
    return max_count,min_count
 
 
# Driver code
arr = [ 7, 8, 4, 5, 4, 1, 1, 7, 7, 2, 5]
n = len(arr)
print(findDiff(arr,n))
 
# This code is contributed by Shrikant13