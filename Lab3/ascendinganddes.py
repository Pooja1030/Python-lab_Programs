#5.1)ascending order
arr=[1,2,9,6,7,3,4]
print("Ascending order is",set(arr))


#5.2)Descending order
arr=[1,2,9,6,7,3,4]
arr1=sorted(arr)
for i in range(len(arr1),0,-1):
    print(arr1[i-1],end=" ")

