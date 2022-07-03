# Program to print elements present at even position
l=eval(input("Enter a list: "))
length=len(l)
print("Array elements present at even position are: ")
for i in range(0,length,2):
    print(l[i],end=' ')