#Program to check if the number is perfect or not
        
n = int(input("Enter a number: "))
s = 0
for i in range(1, n):
    if(n % i == 0):
        s = s + i
if (s == n):
    print("%d is a Perfect Number" %n)
else:
    print("%d is not a Perfect Number" %n)