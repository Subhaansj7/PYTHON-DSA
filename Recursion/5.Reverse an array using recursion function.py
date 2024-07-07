def display(arr,idx,n):
    if idx == 1:
        return
    display(arr,idx+1,n)
    print(arr[idx])