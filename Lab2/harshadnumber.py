# Program to check if the given number is Harshad number
n=int(input("Enter the number: "))
sum=0
for i in str(n):
    sum+=int(i)
if n%sum==0:
    print(n,"is a harshad number")
else:
    print(n,"is not a harshad number")


