#disarium number
num=int(input("Enter a number: "))
sum=0
for i in range(len(str(num))):
    sum+=int(str(num)[i])**(i+1)
if(sum==num):
    print(num,"is a disarium number")
else:
    print(num,"is not a disarium number")
