arr=[2,1,2,3,4,3,5,5,6,2,7,5]

h={}

for i in range(0,len(arr)):
    if arr[i] in h:
        h[arr[i]]=h[arr[i]] + 1
    else:
        h[arr[i]]=1 
        
print(h)