#Program to print the pyramid centre pattern

n = int(input("Enter the number of rows: "))
for i in range(1,n+1):
    s=1
    while s<=n-i:
        print(" ",end='')
        s+=1
    c=1
    while c<=2*i-1:
        print("*",end='')
        c+=1
    print()