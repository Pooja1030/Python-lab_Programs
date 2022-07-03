arr = [4,8,8,8,3,9,4,4,4,25,9,34,9,9]
size = len(arr)
for i in range(size-2):
    if(arr[i] == arr[i+1] and arr[i+1] == arr[i+2]):
        print(arr[i])
    
