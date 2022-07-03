# Armstrong number
n = int(input("Enter a number: "))
l = len(str(n))
sum = 0
temp = n

while temp > 0:
    d = temp % 10
    sum += d**l
    temp //= 10

if n == sum:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")