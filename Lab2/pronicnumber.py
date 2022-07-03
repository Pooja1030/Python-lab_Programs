n = int(input("Enter a number: "))
a = 0
for i in range(n):
    if i * (i + 1) == n:
        a = 1
        break

if a==1:
    print("It is a pronic number")
else:
    print("It is not a pronic number")